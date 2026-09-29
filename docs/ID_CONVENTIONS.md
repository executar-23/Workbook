# Convenção de IDs

Regex canônicas: `registry/workbook.yaml#id_conventions` e `registry/session_b/objects.yaml#object_types`.

| Sessão | Prefixo | Significado | Exemplo |
|---|---|---|---|
| A | `SA-nn` | Seção do Master Index | SA-04 |
| A | `Axx` | Macroárea | A03 |
| A | `Dxx` | Domínio funcional | D12 |
| A | `Dxx.SDyy` | Subdomínio | D12.SD01 |
| A | `Dxx-PRC-nnn` | Processo / ciclo | D08-PRC-001 |
| A | `Dxx-Enn` | Entregável | D12-E04 |
| A | `Dxx-DOC-ACR-nnn` | Documento canônico | D16-DOC-PEM-001 |
| A | `Dxx-DOC-ACR-nnn.secao.campo` | Campo de documento | D01-DOC-TAP-001.scope.fronteiras |
| A | `P00` / `Mn(.n)` | Programa / produto-iniciativa | M2.1 |
| A | `Gnn` (00–11) | Gate | G03 |
| A | `PMnn` (01–13) | Fase do ciclo de produto | PM05 |
| A | `SRC-nn` · `DEC-nnn` · `CNF-nnn` · `GAP-nnn` | Fonte · decisão · conflito · lacuna | CNF-001 |
| A | `ADR-nnn` · `REQ-nnn` | Decisão de arquitetura · requisito | ADR-001 |
| A | `WB-P1-nn` · `WB-Hnn` · `CTR-*` · `Ln` | Workbook · edição HTML · contrato · nível | CTR-INTERFACE |
| A | `Dxx-EVID-nnn` | Evidência de intake (arquivo bruto importado, fora do registry) — vive só em `evidence/`, nunca em `registry/`; classe (`principal/derivado/evidencia/historico/duplicado/obsoleto/em_conflito`) e fonte (`SRC-nn`) em `evidence/master_index.yaml`. Não é documento canônico (`Dxx-DOC-ACR-nnn`) até promoção humana explícita. | D16-EVID-005 |
| A | `GMnn` (01–06) | Grupo Macro — camada acima de `Axx`, agrupando macroáreas (`architecture.yaml#macro_areas[].grupo_macro`) e propagada para cada entrada de `evidence/master_index.yaml` via `Dxx → primary_area (Axx) → GMnn`. Tabela fixa em `evidence/RECLASSIFICACAO_GM01-06.prompt.md#CONSTRAINTS`. | GM05 |
| B | `SB-nn` (00–11) | Seção do Foundation Doc | SB-02 |
| B | `CYC-AAAA-nn` `OBJ-` `RDM-` `BKL-` `SPR-` `TSK-` `ISS-` `PRJ-Mn-` | Ciclo e execução | SPR-001 |
| B | `RB-Dxx-nnn` `ROT-` `CRN-` `TPL-` `AGT-` `CMD-` `EDL-` `WF-XXX-nnn` `SOP-` | Runbook, rotina, cronograma, template, agente, slash command, linha editorial, workflow, procedimento | RB-D08-001 |

Regras: IDs nunca são renumerados nem reutilizados; substituição → `governance.yaml#id_migrations`; aliases de nome em `aliases`; ID novo só com fonte ou decisão humana registrada.
