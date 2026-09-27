#!/usr/bin/env python3
from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError as exc:
    raise SystemExit(f"Dependência ausente: {exc.name}. Instale PyYAML.")

ROOT = Path(__file__).resolve().parents[1]
registry = yaml.safe_load((ROOT / "registry/workbook.yaml").read_text())
schema = yaml.safe_load((ROOT / "schema/workbook.schema.yaml").read_text())

required_root = {"schema_version", "metadata", "agent_contract", "architecture", "portfolio", "governance"}
missing_root = required_root - set(registry)
if missing_root:
    raise SystemExit(f"ERRO: chaves raiz ausentes: {sorted(missing_root)}")
if not re.fullmatch(r"1\.\d+\.\d+", str(registry["schema_version"])):
    raise SystemExit("ERRO: schema_version deve seguir 1.x.x.")
if registry["metadata"].get("id") != "GOV-WORKBOOK-001":
    raise SystemExit("ERRO: metadata.id deve ser GOV-WORKBOOK-001.")

areas = {item["id"] for item in registry["architecture"]["macro_areas"]}
domains = {item["id"] for item in registry["architecture"]["domains"]}
programs = {item["id"] for item in registry["portfolio"]["programs"]}
initiatives = {item["id"] for item in registry["portfolio"]["initiatives"]}
sources = {item["id"] for item in registry["governance"]["sources"]}

collections = [areas, domains, programs, initiatives, {x["id"] for x in registry["governance"]["gates"]}, sources]
all_ids = [value for collection in collections for value in collection]
if len(all_ids) != len(set(all_ids)):
    raise SystemExit("ERRO: IDs duplicados entre coleções.")

patterns = {
    "macroárea": (areas, r"A\d{2}"),
    "domínio": (domains, r"D\d{2}"),
    "programa": (programs, r"P\d{2}"),
    "iniciativa": (initiatives, r"M\d+(?:\.\d+)?"),
    "fonte": (sources, r"SRC-\d{2}"),
}
for label, (values, pattern) in patterns.items():
    invalid = sorted(value for value in values if not re.fullmatch(pattern, value))
    if invalid:
        raise SystemExit(f"ERRO {label}: IDs inválidos: {invalid}")

def require(values, valid, context):
    missing = set(values) - valid
    if missing:
        raise SystemExit(f"ERRO {context}: referências inexistentes: {sorted(missing)}")

for domain in registry["architecture"]["domains"]:
    require([domain["primary_area"]], areas, domain["id"])
    require(domain.get("supporting_areas", []), areas, domain["id"])
    require(domain.get("source_refs", []), sources, domain["id"])

for initiative in registry["portfolio"]["initiatives"]:
    require([initiative["program_id"]], programs, initiative["id"])
    require(initiative["consumes_areas"], areas, initiative["id"])
    require(initiative["consumes_domains"], domains, initiative["id"])
    if "parent_initiative" in initiative:
        require([initiative["parent_initiative"]], initiatives, initiative["id"])

print(f"OK: {len(areas)} macroáreas, {len(domains)} domínios, {len(initiatives)} iniciativas e {len(all_ids)} IDs únicos.")
