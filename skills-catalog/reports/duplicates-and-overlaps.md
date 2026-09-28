# Duplicates and Overlaps Report

Data: 2026-09-27

## Achado principal

`executar-cop` v0.3.0 já chega com as skills **vendorizadas e unificadas**: seu próprio `references/cmd-cop-index.md` declara que, desde a emenda b do ADR-0003 (2026-09-27), as skills antes distribuídas como plugins Anthropic separados (`operations`, `productivity`, `product-management`, `cowork-plugin-management`) foram incorporadas como skills internas sob Apache-2.0 (ver `THIRD_PARTY_NOTICES.md` no pacote de origem). Por isso este catálogo usa `executar-cop/skills/*` como fonte única — não há necessidade de reconciliar os zips soltos desses 4 plugins (mantidos só como histórico em `insumos/EXECUTAR-OPERACOES/`).

## Skills com histórico em mais de um pacote de origem

| Slug | Pacote atual (catalogado) | Pacote(s) anterior(es) (não catalogado(s) separadamente) |
|---|---|---|
| capacity-plan | SKL-OPS-0001 (executar-cop v0.3.0 ou copiloto-operacional) | operations/skills/capacity-plan (idem) |
| change-request | SKL-OPS-0002 (executar-cop v0.3.0 ou copiloto-operacional) | operations/skills/change-request (idem) |
| create-cowork-plugin | SKL-AUT-0002 (executar-cop v0.3.0 ou copiloto-operacional) | cowork-plugin-management/skills/create-cowork-plugin (idem) |
| executar-arvore-roadmap | SKL-DOC-0001 (executar-cop v0.3.0 ou copiloto-operacional) | executar-arvore-roadmap.zip (mesmo pacote, versão solta) |
| executar-mergulhe | SKL-DOC-0002 (executar-cop v0.3.0 ou copiloto-operacional) | EXECUTAR-ARVORE-VISUAL-v1.0.zip/skill/executar-mergulhe (mesmo pacote dentro de entregável maior) |
| executar-plan-mode | SKL-AUT-0003 (executar-cop v0.3.0 ou copiloto-operacional) | executar-plan-mode.zip (mesmo pacote, versão solta) |
| execution-toolkit | SKL-AUT-0004 (executar-cop v0.3.0 ou copiloto-operacional) | EXECUTAR-TAREFAS-full-skill-directory.zip (SKILL.md interno já se autodeclara name: execution-toolkit) |
| memory-management | SKL-PRO-0001 (executar-cop v0.3.0 ou copiloto-operacional) | productivity/skills/memory-management (idem) |
| obsidian-editorial-pipeline | SKL-DOC-0003 (executar-cop v0.3.0 ou copiloto-operacional) | obsidian-editorial-pipeline-v2.2.skill (versão solta, mesmo nome) |
| process-doc | SKL-OPS-0005 (executar-cop v0.3.0 ou copiloto-operacional) | operations/skills/process-doc (idem) |
| product-brainstorming | SKL-PRD-0003 (executar-cop v0.3.0 ou copiloto-operacional) | product-management/skills/product-brainstorming (idem) |
| product-code-development | SKL-PRD-0004 (executar-cop v0.3.0 ou copiloto-operacional) | product-code-development.skill.zip (variante standalone com mais scripts/templates) |
| risk-assessment | SKL-OPS-0007 (executar-cop v0.3.0 ou copiloto-operacional) | operations/skills/risk-assessment (idem) |
| runbook | SKL-OPS-0008 (executar-cop v0.3.0 ou copiloto-operacional) | operations/skills/runbook (plugin Anthropic vendorizado) |
| task-management | SKL-PRO-0003 (executar-cop v0.3.0 ou copiloto-operacional) | productivity/skills/task-management (idem) |
| write-spec | SKL-PRD-0009 (executar-cop v0.3.0 ou copiloto-operacional) | product-management/skills/write-spec (idem) |

## Skills semanticamente próximas (não são duplicatas, mas mesma família)

- `task-management` / `update` / `start` / `memory-management` — todos operam sobre o mesmo `TASKS.md`/memória de sessão (área PRO).
- `runbook` / `process-doc` / `process-optimization` — todos produzem/otimizam documentação de processo operacional (área OPS).
- `create-cowork-plugin` / `cowork-plugin-customizer` — ciclo de vida do mesmo tipo de artefato (criar vs. customizar um plugin Cowork).

## Não incluído no catálogo (com justificativa)

- `anthropic-knowledge-work-plugins.zip` (2.795 arquivos, 17 categorias do marketplace público da Anthropic) — não é skill do usuário.
- `Maestro-Handoff` — pacote de handoff de projeto, não skill executável.
- `CMD-COP-001...docx`, `calendario-light-mode-preview.png`, `dashboard.html` — documentação/assets avulsos.
