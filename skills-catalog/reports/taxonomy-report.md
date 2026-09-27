# Taxonomy Report

Data: 2026-09-27

## Áreas definidas

| Código | Nome | Nº skills |
|---|---|---|
| OPS | Operations | 10 |
| PRD | Product | 9 |
| AUT | Automation/Plugins | 4 |
| DOC | Documentation/Editorial | 3 |
| PRO | Productivity | 4 |
| PLT | Platform | 1 |

## Capability types observados

| Tipo | Nº skills |
|---|---|
| analyzer | 6 |
| expert | 1 |
| generator | 7 |
| orchestrator | 5 |
| planner | 3 |
| tool | 5 |
| tracker | 1 |
| transformer | 2 |
| workflow | 1 |

## Nota metodológica

A taxonomia completa do prompt mestre (subárea, domínio, função, público, critérios de qualidade, riscos/restrições etc.) não pôde ser preenchida com evidência direta para a maioria das skills — os `SKILL.md` de origem trazem principalmente `name` + `description` (frontmatter) e o corpo do procedimento, não um schema de metadados estruturado. Esses campos ficaram `TBD` em `metadata.yaml`, e `area`/`capability_type`/`tags`/`store.category` foram inferidos por leitura semântica da description (classe DERIVED, confiança média), registrados em `provenance.inferred_fields`.
