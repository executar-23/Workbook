# Validation Report

Data: 2026-09-27
Total de skills processadas: 31

## Checagens

- IDs duplicados: nenhum
- Slugs duplicados: nenhum
- YAML válido: sim (todo metadata.yaml carregado com sucesso ao gerar all-skills.yaml)
- Toda skill do input aparece no índice: sim (30 de executar-cop/skills/* + 1 copiloto-operacional = 31)
- Todo ID do índice possui pacote (.skill + metadata.yaml + README.md + source/): sim, gerado programaticamente para as 31
- Todo pacote possui YAML: sim

## Erros encontrados

Nenhum erro bloqueante. Ver `duplicates-and-overlaps.md` para sobreposições de proveniência (não são erros, são achados de proveniência).

## Inferências realizadas (por skill)

Todas as 31 skills tiveram `classification.area`, `classification.capability_type`, `classification.tags` e `store.category` **inferidos** por leitura da description do SKILL.md (classe DERIVED, confiança média) — nenhuma tinha esses campos explícitos na fonte. Ver `provenance.inferred_fields` em cada metadata.yaml. Campos de processo detalhado, inputs/outputs estruturados, dependências formais, critérios de aceite e dados de Store (exceto título/categoria/keywords) permanecem `TBD` por ausência de evidência direta — não foram inventados.
