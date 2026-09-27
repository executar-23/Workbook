#!/usr/bin/env python3
"""Valida o Master Schema EXECUTAR: JSON Schema + integridade referencial + regra Sessão B → Sessão A."""
from pathlib import Path
import re
import sys

try:
    import yaml
    import jsonschema
except ImportError as exc:
    raise SystemExit(f"Dependência ausente: {exc.name}. Execute: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parents[1]


def load(rel):
    return yaml.safe_load((ROOT / rel).read_text(encoding="utf-8"))


def fail(msg):
    raise SystemExit(f"ERRO: {msg}")


registry = load("registry/workbook.yaml")
for session, files in registry.get("includes", {}).items():
    registry[session] = {name: load(path) for name, path in files.items()}



def find_nulls(node, path):
    """Valor nulo quase sempre indica vírgula solta em flow mapping YAML; lacuna deve ser TBD."""
    if isinstance(node, dict):
        for k, v in node.items():
            if v is None:
                fail(f"{path}.{k} é nulo (use TBD ou aspas)")
            find_nulls(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            find_nulls(v, f"{path}[{i}]")


find_nulls(registry, "registry")
schema = load("schema/workbook.schema.yaml")
errors = sorted(jsonschema.Draft202012Validator(schema).iter_errors(registry), key=lambda e: list(e.path))
if errors:
    for e in errors[:20]:
        print(f"ERRO schema em {'/'.join(map(str, e.path)) or '<raiz>'}: {e.message}", file=sys.stderr)
    fail(f"{len(errors)} violações do JSON Schema.")

A, B = registry["session_a"], registry["session_b"]
arch, gov, port, docs = A["architecture"], A["governance"], A["portfolio"], A["documents"]["documents"]

ids_by_kind = {
    "seção SA": [s["id"] for s in A["master_index"]["sections"]],
    "macroárea": [a["id"] for a in arch["macro_areas"]],
    "domínio": [d["id"] for d in arch["domains"]],
    "subdomínio": [s["id"] for d in arch["domains"] for s in d.get("subdomains", [])],
    "entregável": [e["id"] for d in arch["domains"] for s in d.get("subdomains", []) for e in s.get("deliverables", [])],
    "documento": [d["id"] for d in docs],
    "programa": [p["id"] for p in port["programs"]],
    "iniciativa": [m["id"] for m in port["initiatives"]],
    "gate": [g["id"] for g in gov["gates"]],
    "fonte": [s["id"] for s in gov["sources"]],
    "conflito": [c["id"] for c in gov["conflicts"]],
    "gap": [g["id"] for g in gov["gaps"]],
    "decisão": [d["id"] for d in gov["decisions"]],
    "fase PM": [p["id"] for p in A["pm_lifecycle"]["phases"]],
    "workbook": [p["id"] for p in A["workbook_manual"]["parts"]]
    + [c["id"] for p in A["workbook_manual"]["parts"] for c in p.get("chapters", [])]
    + [h["id"] for h in A["workbook_manual"]["html_edition"]["parts"]],
    "nível": [lv["id"] for lv in A["workbook_manual"]["management_levels"]],
    "contrato": [c["id"] for c in A["domain_contracts"]["contracts"].values()],
    "foundation SB": [s["id"] for s in B["foundation"]["foundation_sections"]],
}
b_types = {t["prefix"]: re.compile(f"^{t['id_pattern']}$") for t in B["objects"]["object_types"]}
b_instances = [o for group in B["objects"]["instances"].values() for o in group]
ids_by_kind["objeto B"] = [o["id"] for o in b_instances]

all_ids = [i for ids in ids_by_kind.values() for i in ids]
dupes = sorted({i for i in all_ids if all_ids.count(i) > 1})
if dupes:
    fail(f"IDs duplicados: {dupes}")

session_a_ids = set(all_ids) - set(ids_by_kind["foundation SB"]) - set(ids_by_kind["objeto B"])
areas, domains = set(ids_by_kind["macroárea"]), set(ids_by_kind["domínio"])
doc_ids, sources = set(ids_by_kind["documento"]), set(ids_by_kind["fonte"])
initiatives, programs = set(ids_by_kind["iniciativa"]), set(ids_by_kind["programa"])


def require(values, valid, context):
    missing = set(values) - set(valid)
    if missing:
        fail(f"{context}: referências inexistentes: {sorted(missing)}")


def walk_source_refs(node, context):
    if isinstance(node, dict):
        require(node.get("source_refs", []), sources, context)
        for k, v in node.items():
            walk_source_refs(v, f"{context}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk_source_refs(v, f"{context}[{i}]")


walk_source_refs(A, "session_a")
walk_source_refs(B, "session_b")

# Domínios: parent Axx, documentos existentes e do próprio domínio, prefixo de subdomínios/entregáveis
for d in arch["domains"]:
    require([d["primary_area"]] + d.get("supporting_areas", []), areas, d["id"])
    require(d["documents"], doc_ids, d["id"])
    for sd in d.get("subdomains", []):
        if not sd["id"].startswith(d["id"] + "."):
            fail(f"{sd['id']} não pertence a {d['id']}")
        for e in sd.get("deliverables", []):
            if not e["id"].startswith(d["id"] + "-"):
                fail(f"{e['id']} não pertence a {d['id']}")

# Documentos: 37 = 23 MACRO + 14 SPECIALIZED; um MACRO por domínio; listados no domínio
macro = [x for x in docs if x["document_class"] == "MACRO"]
spec = [x for x in docs if x["document_class"] == "SPECIALIZED"]
if (len(docs), len(macro), len(spec)) != (37, 23, 14):
    fail(f"esperado 37/23/14 documentos, obtido {len(docs)}/{len(macro)}/{len(spec)}")
if sorted(x["domain_id"] for x in macro) != sorted(domains):
    fail("cada domínio precisa de exatamente um documento MACRO")
listed = {ref: d["id"] for d in arch["domains"] for ref in d["documents"]}
for x in docs:
    if not x["id"].startswith(x["domain_id"] + "-"):
        fail(f"{x['id']}: prefixo difere de domain_id {x['domain_id']}")
    if listed.get(x["id"]) != x["domain_id"]:
        fail(f"{x['id']} não está listado em {x['domain_id']}.documents")
    if x["approval_status"] == "APROVADO" or x["document_status"] not in ("IDENTIFICADO", "PRE_PREENCHIDO"):
        fail(f"{x['id']}: promoção de estado sem evidência humana registrada")

# Contratos de domínio: um por domínio, identidade coerente
contracts = A["domain_contracts"]["domain_contracts"]
if sorted(c["domain_id"] for c in contracts) != sorted(domains):
    fail("domain_contracts deve ter exatamente um contrato por D01–D23")
for c in contracts:
    ident = c["playbook"]["identidade"]
    if isinstance(ident, dict) and ident.get("ref") != c["domain_id"]:
        fail(f"contrato {c['domain_id']}: identidade.ref divergente")
    for e in c["playbook"]["entregaveis"] if isinstance(c["playbook"]["entregaveis"], list) else []:
        require([e["ref"]], doc_ids, f"contrato {c['domain_id']}")

# Portfólio
for m in port["initiatives"]:
    require([m["program_id"]], programs, m["id"])
    require(m["consumes_areas"], areas, m["id"])
    require(m["consumes_domains"], domains, m["id"])
    if "parent_initiative" in m:
        require([m["parent_initiative"]], initiatives, m["id"])
    for cap in m.get("capability_map", []):
        require([cap["area"]], areas, f"{m['id']}.capability_map")
        if "domain" in cap:
            require([cap["domain"]], domains, f"{m['id']}.capability_map")
gap_ids = set(ids_by_kind["gap"])
for f in port["ecosystem_fronts"]:
    require(f["initiatives"], initiatives, f"frente {f['label']}")
    require(f.get("related_domains", []), domains, f"frente {f['label']}")
    if not f["initiatives"] and f.get("gap_ref") not in gap_ids:
        fail(f"frente {f['label']} sem iniciativa precisa de gap_ref válido")

# Sessão B → Sessão A
FORBIDDEN_B = {"sections", "record_schema", "definition", "purpose_canonical"}
b_objects = B["foundation"]["foundation_sections"] + b_instances
for o in b_objects:
    if not o.get("refs_a"):
        fail(f"{o['id']}: objeto da Sessão B sem refs_a")
    require(o["refs_a"], session_a_ids, f"{o['id']}.refs_a")
    leaked = FORBIDDEN_B & set(o)
    if leaked:
        fail(f"{o['id']}: conhecimento canônico duplicado na Sessão B: {sorted(leaked)}")
for o in b_instances:
    if not any(p.match(o["id"]) for p in b_types.values()):
        fail(f"{o['id']}: prefixo/ID não corresponde a nenhum object_type da Sessão B")
for t in B["objects"]["object_types"]:
    if "shape_ref" in t:
        require([t["shape_ref"]], doc_ids, f"object_type {t['prefix']}")
for step in B["execution_flow"]["cycle_flow"]:
    require(step.get("refs_a", []), session_a_ids, step["id"])
require(B["execution_flow"]["prefill_execution_graph"]["refs_a"], session_a_ids, "WF-PREFILL-001")

print(
    f"OK: {len(areas)} macroáreas, {len(domains)} domínios, {len(ids_by_kind['subdomínio'])} subdomínios, "
    f"{len(docs)} documentos ({len(macro)} macro/{len(spec)} especializados), {len(initiatives)} iniciativas, "
    f"{len(ids_by_kind['gate'])} gates, {len(sources)} fontes, {len(ids_by_kind['seção SA'])} seções SA, "
    f"{len(ids_by_kind['foundation SB'])} seções SB, {len(gov['conflicts'])} conflitos, {len(gov['gaps'])} gaps, "
    f"{len(all_ids)} IDs únicos."
)
