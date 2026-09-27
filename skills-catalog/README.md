# Skills Catalog — EXECUTAR

Catálogo mestre gerado em 2026-09-27 a partir de `insumos/EXECUTAR-COP-V0.3.0` e
`insumos/COPILOTO-OPERACIONAL` (ver `insumos/SOURCE_REGISTER.yaml`, `INS-014`/`INS-015`).

**31 skills catalogadas.** `anthropic-knowledge-work-plugins.zip` (marketplace público
da Anthropic, 2.795 arquivos) e os zips já superados pela vendorização do ADR-0003 do próprio
`executar-cop` **não** foram recatalogados — ver `reports/duplicates-and-overlaps.md`.

## Estrutura

- `master-index/` — `master-skill-index.csv` / `.xlsx` (com aba `EXECUTIVE_SUMMARY`) / `.md`
- `skills/SKL-<AREA>-nnnn__<slug>/` — pacote por skill: `.skill` (zip), `metadata.yaml`, `README.md`, `source/`
- `yaml/` — espelho de cada `metadata.yaml` + `all-skills.yaml` agregado
- `reports/` — `validation-report.md`, `duplicates-and-overlaps.md`, `taxonomy-report.md`
- `MANIFEST.yaml` — IDs, áreas e relações principais
- `skills-catalog-final.zip` — empacotamento de tudo acima

## Disciplina epistêmica

Nenhum campo foi inventado. `classification.area/capability_type/tags` e `store.category` foram
**inferidos** por leitura da `description` de cada `SKILL.md` (classe DERIVED, confiança média) e
estão listados em `provenance.inferred_fields` de cada `metadata.yaml`. Campos sem evidência
direta (processo detalhado, inputs/outputs estruturados, dependências formais, critérios de
aceite, dados de Solution Store além de título/categoria/keywords) ficam `TBD`.
