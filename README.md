# Workbook EXECUTAR

Este `README.md` é o próprio Workbook — capa, índice e as 17 páginas
`WB-H01`–`WB-H17` são construídas e populadas aqui, conforme
`CLAUDE.md#construção-e-população-do-workbook`. Sem deep links nem
hiperlinks entre páginas; IDs são texto plano, localizáveis por busca.

---

## CAPA

| Campo | Valor |
|---|---|
| ID | `GOV-WORKBOOK-001` |
| Título | Sistema Integrado de Governança e Operação EXECUTAR |
| Versão | `1.1.0` (`registry/workbook.yaml#schema_version`) |
| Data da consolidação | 2026-09-27 (`registry/workbook.yaml#metadata.updated_at`) |
| Situação documental | `proposed` |
| Período coberto | TBD (sem fonte) |

---

## ÍNDICE

Tabela plana, sem links. Localizar uma página pelo ID via busca textual no
próprio arquivo (ex.: buscar `WB-H05`). Atualizar esta tabela no mesmo
commit que adicionar, editar ou mudar o status de qualquer página —
conferir esta regra em `CLAUDE.md` antes de fechar a edição.

| ID | Nome | Mapeamento | Status | Última atualização |
|---|---|---|---|---|
| WB-H01 | Visão Executiva | WB-P1 | vazio — aguardando população | — |
| WB-H02 | Governança | WB-P1 | vazio — aguardando população | — |
| WB-H03 | Cadeia de Valor | WB-P1 | vazio — aguardando população | — |
| WB-H04 | Áreas do Ecossistema | WB-P2 | rascunho — GM01 populado, GM02–06 pendentes | 2026-09-29 |
| WB-H05 | Portfólio | WB-P1 | vazio — aguardando população | — |
| WB-H06 | Planejamento (estratégico/tático/operacional) | WB-P3 | vazio — aguardando população | — |
| WB-H07 | Roteiro de Evolução (agora/próximo/futuro) | WB-P3 | vazio — aguardando população | — |
| WB-H08 | Ciclos de Trabalho | WB-P3 | vazio — aguardando população | — |
| WB-H09 | Processos | WB-P2 | vazio — aguardando população | — |
| WB-H10 | Interfaces entre Áreas | WB-P2 | vazio — aguardando população | — |
| WB-H11 | Dados e Fontes Principais | WB-P1 | vazio — aguardando população | — |
| WB-H12 | Documentos e Evidências | WB-P1 | rascunho — GM01 populado, GM02–06 pendentes | 2026-09-29 |
| WB-H13 | Riscos Problemas e Bloqueios | WB-P3 | vazio — aguardando população | — |
| WB-H14 | Indicadores | WB-P1 | vazio — aguardando população | — |
| WB-H15 | Painel Executivo | WB-P3 | vazio — aguardando população | — |
| WB-H16 | Lacunas e Decisões Pendentes | SA-10 | rascunho — GM01 populado, GM02–06 pendentes | 2026-09-29 |
| WB-H17 | Rastreabilidade | SA-00 | vazio — aguardando população | — |

Fonte da lista de páginas: `registry/session_a/workbook_manual.yaml#html_edition.parts`.

### Painel de Completude

Progresso: 0/17 páginas com status `populado` (0%) — 3/17 em `rascunho`.
Recalculado mecanicamente a cada execução de
`docs/prompts/POPULAR_AREA_WORKBOOK.prompt.md`; não editar à mão.

| Grande Macro | Páginas WB-H afetadas até agora | Status |
|---|---|---|
| GM01 Estratégia, Governança e Corporativo | WB-H04, WB-H12, WB-H16 | processado |
| GM02 Negócio, Mercado e Growth | — | pendente |
| GM03 Produto e Experiência | — | pendente |
| GM04 Engenharia, Plataforma e Operações | — | pendente |
| GM05 Dados, Conhecimento e Documentação | — | pendente |
| GM06 Execução, Automação e Ferramentas | — | pendente |

---

## WB-H04 · Áreas do Ecossistema — Página

`mapeamento: WB-P2` · `status: rascunho` · `atualizado: 2026-09-29`

Fatia GM01 (Estratégia, Governança e Corporativo). Fonte:
`registry/session_a/architecture.yaml#macro_areas`/`domains`.

| Macroárea | Finalidade | Domínios | Grupo Macro |
|---|---|---|---|
| A00 Governança Estratégia e Gestão | Direção decisões planejamento e controles | D01, D22 | GM01 |
| A07 Corporativo e Suporte | Funções empresariais estruturantes | D02, D03, D04 | GM01 |
| A12 Stakeholders e Ecossistema | Relações com atores parceiros fornecedores e comunidade | D17 | GM01 |

| Domínio | Nome | Área principal | Áreas de apoio |
|---|---|---|---|
| D01 | Gestão Empresarial | A00 | — |
| D02 | Jurídico Riscos e Conformidade | A07 | A00 |
| D03 | Finanças | A07 | A00 |
| D04 | Pessoas e RH | A07 | — |
| D17 | Emprego e Portfólio | A12 | — |
| D22 | Decision and Register Log | A00 | A10 |

GM02–GM06 (A01–A09, A11) ficam `TBD` até a execução deste prompt para
essas áreas.

--- fim da página WB-H04 ---

## WB-H12 · Documentos e Evidências — Página

`mapeamento: WB-P1` · `status: rascunho` · `atualizado: 2026-09-29`

Fatia GM01. Fonte: `registry/session_a/documents.yaml` (documentos
canônicos) e `evidence/master_index.yaml` (evidência de intake).

### Documentos canônicos (GM01)

| ID | Nome | Domínio | Classe | Estado do documento | Aprovação |
|---|---|---|---|---|---|
| D01-DOC-DDE-001 | Documento de Direção Empresarial | D01 | MACRO | PRE_PREENCHIDO | PENDENTE |
| D01-DOC-TAP-001 | Termo de Abertura do Ecossistema | D01 | SPECIALIZED | PRE_PREENCHIDO | PENDENTE |
| D01-DOC-MNE-001 | Modelo de Negócio do Ecossistema | D01 | SPECIALIZED | PRE_PREENCHIDO | PENDENTE |
| D01-DOC-MRE-001 | Mapa de Relações do Ecossistema | D01 | SPECIALIZED | PRE_PREENCHIDO | PENDENTE |
| D02-DOC-DGRC-001 | Documento de Governança, Riscos e Conformidade | D02 | MACRO | PRE_PREENCHIDO | PENDENTE |
| D02-DOC-MRC-001 | Matriz de Riscos e Controles | D02 | SPECIALIZED | PRE_PREENCHIDO | PENDENTE |
| D02-DOC-PPT-001 | Política de Privacidade e Termos | D02 | SPECIALIZED | PRE_PREENCHIDO | PENDENTE |
| D03-DOC-PFO-001 | Plano Financeiro e Orçamentário | D03 | MACRO | PRE_PREENCHIDO | PENDENTE |
| D03-DOC-MFO-001 | Modelo Financeiro do Ecossistema | D03 | SPECIALIZED | PRE_PREENCHIDO | PENDENTE |
| D04-DOC-PPC-001 | Plano de Pessoas e Capacidade | D04 | MACRO | PRE_PREENCHIDO | PENDENTE |
| D17-DOC-PEP-001 | Plano de Emprego e Portfólio | D17 | MACRO | PRE_PREENCHIDO | PENDENTE |
| D22-DOC-DRL-001 | Decision and Register Log do Ecossistema | D22 | MACRO | PRE_PREENCHIDO | PENDENTE |

Nenhum dos 12 tem seção de conteúdo preenchida ainda — `sections` no
registry é só o esquema de campos, não o valor. Ver `documents.yaml`.

### Evidência de intake (GM01)

D01, D02, D03, D04 e D22 não têm nenhum arquivo em `evidence/` ainda. D17
(Emprego e Portfólio) tem 13:

| ID | Nome original | Classe |
|---|---|---|
| D17-EVID-001 | Contexto | evidencia |
| D17-EVID-002 | Carreira Applied AI na Europa — decisões até 18/02/2027 | evidencia |
| D17-EVID-003 | PROJECT_CHARTER_CICLO_01_AI_EUROPA_2026_27.csv | evidencia |
| D17-EVID-004 | ai_europa_decisoes_2026_2027.json | evidencia |
| D17-EVID-005 | Estratégia | evidencia |
| D17-EVID-006 | Gtm profissional | evidencia |
| D17-EVID-007 | Prompt | evidencia |
| D17-EVID-008 | claude/PLANO_MESTRE_CICLO_01.md | evidencia |
| D17-EVID-009 | claude/CAPABILITY_MATRIX_CICLO_01.md | evidencia |
| D17-EVID-010 | claude/BACKLOG_CICLO_01.csv | evidencia |
| D17-EVID-011 | claude/PACOTE_SPRINT_01.md | evidencia |
| D17-EVID-012 | claude/FUNIL_CANDIDATURAS.csv | evidencia |
| D17-EVID-013 | career-ai-europe.md | evidencia |

Tudo `status: proposed` — nenhum promovido a canônico.

--- fim da página WB-H12 ---

## WB-H16 · Lacunas e Decisões Pendentes — Página

`mapeamento: SA-10` · `status: rascunho` · `atualizado: 2026-09-29`

Fatia GM01. Fonte: `registry/session_a/governance.yaml#gaps`/`conflicts`
— só itens que bloqueiam ou tocam diretamente governança/domínios GM01.

| ID | Lacuna/Conflito | Impacto | Quem decide | O que desbloqueia |
|---|---|---|---|---|
| GAP-006 | Fontes SRC-01…SRC-05 citadas no Business Docs original (Governança Operacional) e os 1.125 campos do Control Plane não foram fornecidos | Control Plane (SA-06) incompleto | humano (fonte original) | SA-06 |
| GAP-007 | Nomes e critérios de aceite dos gates G01–G11 | Gates sem critério de aceite | decisão humana | gates |
| GAP-008 | Owners de macroáreas, domínios e documentos | Nenhum documento GM01 tem owner definido | decisão humana | domain_contracts |
| CNF-007 | Regra de commit — `AGENTS.md` (commit direto em `main`) × instrução da sessão de automação (branch dedicada + PR) | Ambiguidade de processo de governança de mudança | decisão humana | regra permanente de commit |

GM02–GM06 ficam `TBD` até a execução deste prompt para essas áreas.

--- fim da página WB-H16 ---

## Sobre este repositório

Fonte canônica, versionada e legível por máquina do Master Schema do ecossistema EXECUTAR (GOV-WORKBOOK-001), separando:

- **Sessão A — Consulta / Knowledge System** (`registry/session_a/`): o que o sistema é e conhece.
- **Sessão B — Produção / Execution System** (`registry/session_b/`): como o sistema executa, sempre referenciando IDs da Sessão A.

### Estrutura

| Caminho | Conteúdo |
|---|---|
| `registry/workbook.yaml` | Raiz: metadata, contrato de agentes, includes, convenções de IDs |
| `registry/session_a/master_index.yaml` | Master Index SA-00…SA-12 + padrão transversal |
| `registry/session_a/architecture.yaml` | A00–A12, D01–D23, subdomínios e entregáveis |
| `registry/session_a/domain_contracts.yaml` | Playbook (21 campos) + Interface Contract por domínio |
| `registry/session_a/documents.yaml` | 37 documentos canônicos (23 macro + 14 especializados) |
| `registry/session_a/portfolio.yaml` | P00, M0–M16, frentes do ecossistema |
| `registry/session_a/governance.yaml` | Gates, estados, modelo epistêmico, fontes, conflitos, gaps, decisões |
| `registry/session_a/workbook_manual.yaml` | Partes I–III, matriz fractal, L0–L6, edição HTML |
| `registry/session_a/pm_lifecycle.yaml` | PM01–PM13 |
| `registry/session_b/*.yaml` | Foundation Doc SB-00…11, fluxo do ciclo, tipos/instâncias de objetos |
| `schema/workbook.schema.yaml` | JSON Schema do documento consolidado |
| `scripts/validate.py` | Schema + integridade referencial + regra B→A |
| `docs/` | Arquitetura, IDs, navegação, protocolo de agentes |
| `assets/design-system/` | Tokens + componentes da edição HTML do Workbook (WB-H01–H17), deliverable `D21-E01` — `status: proposed` |
| `evidence/` | Insumo bruto classificado por domínio (`Dxx-EVID-nnn`) e grupo macro (`GMnn`), aguardando promoção humana |

### Validação

```bash
pip install -r requirements.txt
python scripts/validate.py
```

Toda alteração mantém IDs estáveis, referências válidas, separação capacidades × portfólio e Sessão A × Sessão B. Lacunas são `TBD`.
