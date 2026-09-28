# D01 — Agent Index

**Bundle ID:** `D01-BUNDLE-UNIFIED-001`  
**Canonical bundle:** `01_YAML_BUNDLE.yaml`  
**Purpose:** deterministic navigation and provenance across the specialized TAP schema and the PRIMARY_CORPUS.

## 1. Source registry

| Source ID | File | Role | SHA-256 |
|---|---|---|---|
| `SRC-YAML-TAP-001` | `D01-DOC-TAP-001.yaml` | `SPECIALIZED_SCHEMA` | `26246f4ccf7b5bfa8a2495bff8a710ecce584678b690e88ebc4e82f8299d6e77` |
| `SRC-DOCX-PRIMARY-001` | `D01-Executar Ecossitema__PRIMARY_CORPUS.docx` | `PRIMARY_CORPUS` | `0ee95d2e5732817a304348bddd446261edc070bd9bb6daf65fc39bf48d652af0` |

> The two inputs are **not declared equivalent**. They are unified for navigation while their original bytes/text remain preserved.

## 2. Authority and agent rules

1. `source_payloads` is immutable source evidence.
2. `normalized_index` is navigation/derivation metadata, not a replacement for the source.
3. TAP `candidate_evidence_refs` are candidates only; do not auto-fill `resposta` from them.
4. Preserve `A_CONFIRMAR`, `TBD`, conflicts and historical statements unless a supplied source explicitly resolves them.
5. When a later passage explicitly corrects an earlier one, use `source_asserted_corrections` as precedence metadata and retain both passages.

## 3. ID grammar

| ID | Meaning |
|---|---|
| `D01-DOC-TAP-001.<SECTION>.<FIELD>` | Original TAP trace field |
| `D01-PRIMARY.P#####` | Exact DOCX paragraph/block |
| `TOP-###` | Explicit topic in PRIMARY_CORPUS |
| `FORM-##` | Explicit closure/source form in PRIMARY_CORPUS |
| `CORR-###` | Source-declared correction/precedence record |

## 4. TAP field index

Original artifact: `D01-DOC-TAP-001` — Termo de Abertura do Ecossistema. Fields: **29**.

| Trace ID | Section | Original field | Mapping status |
|---|---|---|---|
| `D01-DOC-TAP-001.IDENTIFICATION.TITULO` | Identification | `titulo` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.IDENTIFICATION.JUSTIFICATIVA` | Identification | `justificativa` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.IDENTIFICATION.CONTEXTO` | Identification | `contexto` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.IDENTIFICATION.SPONSOR` | Identification | `sponsor` | `NO_DIRECT_LEXICAL_EVIDENCE` |
| `D01-DOC-TAP-001.IDENTIFICATION.OWNER` | Identification | `owner` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.OBJECTIVE.OBJETIVO_GERAL` | Objective | `objetivo_geral` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.OBJECTIVE.OBJETIVOS_ESPECIFICOS` | Objective | `objetivos_especificos` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.OBJECTIVE.RESULTADO_FINAL_ESPERADO` | Objective | `resultado_final_esperado` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.SCOPE.ESCOPO_INCLUIDO` | Scope | `escopo_incluido` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.SCOPE.ESCOPO_EXCLUIDO` | Scope | `escopo_excluido` | `NO_DIRECT_LEXICAL_EVIDENCE` |
| `D01-DOC-TAP-001.SCOPE.FRONTEIRAS` | Scope | `fronteiras` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.DELIVERABLES.ENTREGAVEIS_PRINCIPAIS` | Deliverables | `entregaveis_principais` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.DELIVERABLES.DEFINITION_OF_DONE` | Deliverables | `definition_of_done` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.MILESTONES.MARCOS` | Milestones | `marcos` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.MILESTONES.DATAS_EXISTENTES` | Milestones | `datas_existentes` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.STAKEHOLDERS.PARTICIPANTES` | Stakeholders | `participantes` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.STAKEHOLDERS.PAPEIS` | Stakeholders | `papeis` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.STAKEHOLDERS.RESPONSABILIDADES` | Stakeholders | `responsabilidades` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.CONSTRAINTS.RESTRICOES` | Constraints | `restricoes` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.CONSTRAINTS.PREMISSAS` | Constraints | `premissas` | `NO_DIRECT_LEXICAL_EVIDENCE` |
| `D01-DOC-TAP-001.CONSTRAINTS.DEPENDENCIAS` | Constraints | `dependencias` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.RESOURCES.CAPACIDADE` | Resources | `capacidade` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.RESOURCES.RECURSOS` | Resources | `recursos` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.RESOURCES.ORCAMENTO` | Resources | `orcamento` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.SUCCESS.CRITERIOS_DE_ACEITE` | Success | `criterios_de_aceite` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.SUCCESS.INDICADORES_DE_SUCESSO` | Success | `indicadores_de_sucesso` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.RISKS.RISCOS_INICIAIS` | Risks | `riscos_iniciais` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.APPROVALS.APROVADORES` | Approvals | `aprovadores` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |
| `D01-DOC-TAP-001.APPROVALS.STATUS_APROVACAO` | Approvals | `status_aprovacao` | `UNRESOLVED_REQUIRES_HUMAN_OR_AGENT_REVIEW` |

### TAP audit

- Declared fields: **29**; actual: **29**; unique trace IDs: **29**.
- `resposta=null`: **29/29**.
- `evidencia_ou_link_obsidian=null`: **29/29**.
- `decisao_ou_observacao=null`: **29/29**.
- `aplicabilidade=A_CONFIRMAR`: **29/29**.

## 5. PRIMARY_CORPUS index

Exact text extraction: **4287 paragraphs** (3328 non-empty). Explicit topics indexed: **75**. Forms indexed: **6**.

### Forms

| ID | Title | Source range |
|---|---|---|
| `FORM-01` | FORM-01 — Estratégia Comercial EXECUTAR | `D01-PRIMARY.P00908` → `D01-PRIMARY.P00929` |
| `FORM-02` | FORM-02 — Multi-Agent SDK Blueprint | `D01-PRIMARY.P00930` → `D01-PRIMARY.P00951` |
| `FORM-03` | FORM-03 — EXECUTAR App · Arquitetura, Fluxos e Customer Journey | `D01-PRIMARY.P00952` → `D01-PRIMARY.P00973` |
| `FORM-04` | FORM-04 — Metodologia + Agent Contract | `D01-PRIMARY.P00974` → `D01-PRIMARY.P00994` |
| `FORM-05` | FORM-05 — Agent Maestro | `D01-PRIMARY.P00995` → `D01-PRIMARY.P01015` |
| `FORM-06` | FORM-06 — EXECUTAR Family Skills | `D01-PRIMARY.P01016` → `D01-PRIMARY.P01037` |

### Topics

| ID | Title | Source range |
|---|---|---|
| `TOP-001` | TOP-001 — Posicionamento Comercial EXECUTAR | `D01-PRIMARY.P01141` → `D01-PRIMARY.P01144` |
| `TOP-002` | TOP-002 — Governança e Produção Audiovisual GTM | `D01-PRIMARY.P01183` → `D01-PRIMARY.P01186` |
| `TOP-003` | TOP-003 — EXECUTAR App — Visão Sistêmica Mestre | `D01-PRIMARY.P01225` → `D01-PRIMARY.P01228` |
| `TOP-004` | TOP-004 — Sitemap e Rotas do EXECUTAR App | `D01-PRIMARY.P01267` → `D01-PRIMARY.P01270` |
| `TOP-005` | TOP-005 — Customer Journey — 25 Etapas | `D01-PRIMARY.P01309` → `D01-PRIMARY.P01312` |
| `TOP-006` | TOP-006 — Customer Journey — Experiência por Fase | `D01-PRIMARY.P01351` → `D01-PRIMARY.P01354` |
| `TOP-007` | TOP-007 — Copiloto — Workflow Agentic | `D01-PRIMARY.P01393` → `D01-PRIMARY.P01396` |
| `TOP-008` | TOP-008 — Comandos do Copiloto | `D01-PRIMARY.P01435` → `D01-PRIMARY.P01438` |
| `TOP-009` | TOP-009 — Modo Rotina e Automações | `D01-PRIMARY.P01477` → `D01-PRIMARY.P01480` |
| `TOP-010` | TOP-010 — Domínio, Dados e Estados | `D01-PRIMARY.P01519` → `D01-PRIMARY.P01522` |
| `TOP-011` | TOP-011 — Arquitetura Técnica do EXECUTAR App | `D01-PRIMARY.P01561` → `D01-PRIMARY.P01564` |
| `TOP-012` | TOP-012 — Scanner Visual EXECUTAR | `D01-PRIMARY.P01603` → `D01-PRIMARY.P01606` |
| `TOP-013` | TOP-013 — Mapa-OS / Prisma | `D01-PRIMARY.P01645` → `D01-PRIMARY.P01648` |
| `TOP-014` | TOP-014 — Status Report EXECUTAR | `D01-PRIMARY.P01687` → `D01-PRIMARY.P01690` |
| `TOP-015` | TOP-015 — Multi-Agent SDK Blueprint | `D01-PRIMARY.P01729` → `D01-PRIMARY.P01732` |
| `TOP-016` | TOP-016 — Governança e System Manifest Multi-Agent | `D01-PRIMARY.P01771` → `D01-PRIMARY.P01774` |
| `TOP-017` | TOP-017 — Orquestrador Multi-Agent | `D01-PRIMARY.P01813` → `D01-PRIMARY.P01816` |
| `TOP-018` | TOP-018 — Agentes Especializados | `D01-PRIMARY.P01855` → `D01-PRIMARY.P01858` |
| `TOP-019` | TOP-019 — Contrato de Handoff | `D01-PRIMARY.P01897` → `D01-PRIMARY.P01900` |
| `TOP-020` | TOP-020 — Skill Registry Multi-Agent | `D01-PRIMARY.P01939` → `D01-PRIMARY.P01942` |
| `TOP-021` | TOP-021 — Tool Registry Multi-Agent | `D01-PRIMARY.P01981` → `D01-PRIMARY.P01984` |
| `TOP-022` | TOP-022 — Context Sources Multi-Agent | `D01-PRIMARY.P02023` → `D01-PRIMARY.P02026` |
| `TOP-023` | TOP-023 — Memory & State Multi-Agent | `D01-PRIMARY.P02065` → `D01-PRIMARY.P02068` |
| `TOP-024` | TOP-024 — Policies, Guardrails e Permission Matrix | `D01-PRIMARY.P02107` → `D01-PRIMARY.P02110` |
| `TOP-025` | TOP-025 — Main Workflow Multi-Agent | `D01-PRIMARY.P02149` → `D01-PRIMARY.P02152` |
| `TOP-026` | TOP-026 — Output Schema Final Multi-Agent | `D01-PRIMARY.P02191` → `D01-PRIMARY.P02194` |
| `TOP-027` | TOP-027 — Evals e Acceptance Gate Multi-Agent | `D01-PRIMARY.P02233` → `D01-PRIMARY.P02236` |
| `TOP-028` | TOP-028 — Observability / Tracing Multi-Agent | `D01-PRIMARY.P02275` → `D01-PRIMARY.P02278` |
| `TOP-029` | TOP-029 — Runtime Config Multi-Agent | `D01-PRIMARY.P02317` → `D01-PRIMARY.P02320` |
| `TOP-030` | TOP-030 — Deployment Multi-Agent | `D01-PRIMARY.P02359` → `D01-PRIMARY.P02362` |
| `TOP-031` | TOP-031 — Plano de Testes Multi-Agent | `D01-PRIMARY.P02401` → `D01-PRIMARY.P02404` |
| `TOP-032` | TOP-032 — MTD-001 — ACTION UNIT / Semântica Adaptativa | `D01-PRIMARY.P02443` → `D01-PRIMARY.P02446` |
| `TOP-033` | TOP-033 — MTD-002 — Good Path / Bad Path para ACTION UNIT | `D01-PRIMARY.P02485` → `D01-PRIMARY.P02488` |
| `TOP-034` | TOP-034 — MTD-003 — PLAN-CARD-5X (Legado) | `D01-PRIMARY.P02527` → `D01-PRIMARY.P02530` |
| `TOP-035` | TOP-035 — MTD-004 — Fixtures PLAN-CARD-5X (Legado) | `D01-PRIMARY.P02569` → `D01-PRIMARY.P02572` |
| `TOP-036` | TOP-036 — MTD-005 — Planejamento Adaptativo Agent SDK | `D01-PRIMARY.P02611` → `D01-PRIMARY.P02614` |
| `TOP-037` | TOP-037 — MTD-006 — Controle de Entregáveis e Ergonomia Cognitiva | `D01-PRIMARY.P02653` → `D01-PRIMARY.P02656` |
| `TOP-038` | TOP-038 — MTD-007 — Evidências TDAH × Gestão de Projetos | `D01-PRIMARY.P02695` → `D01-PRIMARY.P02698` |
| `TOP-039` | TOP-039 — MTD-008 — Matriz Neurodesign de Produto | `D01-PRIMARY.P02737` → `D01-PRIMARY.P02740` |
| `TOP-040` | TOP-040 — RGR-001 — Design: Espaçamento, Grade e Hierarquia | `D01-PRIMARY.P02779` → `D01-PRIMARY.P02782` |
| `TOP-041` | TOP-041 — RGR-002 — Painel Operacional Impresso A4 | `D01-PRIMARY.P02821` → `D01-PRIMARY.P02824` |
| `TOP-042` | TOP-042 — RGR-003 — Contraste e Paleta para Impressão | `D01-PRIMARY.P02863` → `D01-PRIMARY.P02866` |
| `TOP-043` | TOP-043 — RGR-004 — Semântica vs Renderização | `D01-PRIMARY.P02905` → `D01-PRIMARY.P02908` |
| `TOP-044` | TOP-044 — Agent Maestro — Cross-Functional Knowledge Orchestrator | `D01-PRIMARY.P02947` → `D01-PRIMARY.P02950` |
| `TOP-045` | TOP-045 — EXECUTAR Árvore Visual | `D01-PRIMARY.P02989` → `D01-PRIMARY.P02992` |
| `TOP-046` | TOP-046 — Skill EXECUTAR Mergulhe | `D01-PRIMARY.P03031` → `D01-PRIMARY.P03034` |
| `TOP-047` | TOP-047 — EXECUTAR MCP Skill Contract V2.1 | `D01-PRIMARY.P03073` → `D01-PRIMARY.P03076` |
| `TOP-048` | TOP-048 — Executar ADPTER → JSON (Legado/Migrado) | `D01-PRIMARY.P03115` → `D01-PRIMARY.P03118` |
| `TOP-049` | TOP-049 — Executar Divisão de Tarefas — Contrato Legado | `D01-PRIMARY.P03157` → `D01-PRIMARY.P03160` |
| `TOP-050` | TOP-050 — Executar Divisão de Tarefas Public v2 — Texto → Plan Exchange | `D01-PRIMARY.P03199` → `D01-PRIMARY.P03202` |
| `TOP-051` | TOP-051 — Agents SDK Handoff V2 + MCP | `D01-PRIMARY.P03241` → `D01-PRIMARY.P03244` |
| `TOP-052` | TOP-052 — Project Reconstructor Agent SDK | `D01-PRIMARY.P03283` → `D01-PRIMARY.P03286` |
| `TOP-053` | TOP-053 — Prisma Dashboard Population Skill | `D01-PRIMARY.P03325` → `D01-PRIMARY.P03328` |
| `TOP-054` | TOP-054 — Executar Design | `D01-PRIMARY.P03367` → `D01-PRIMARY.P03370` |
| `TOP-055` | TOP-055 — DeskGo Business Workbook | `D01-PRIMARY.P03409` → `D01-PRIMARY.P03412` |
| `TOP-056` | TOP-056 — Gerar Workbook DeskGo — Swiss | `D01-PRIMARY.P03451` → `D01-PRIMARY.P03454` |
| `TOP-057` | TOP-057 — Executar Árvore Roadmap | `D01-PRIMARY.P03493` → `D01-PRIMARY.P03496` |
| `TOP-058` | TOP-058 — Executar Calendar | `D01-PRIMARY.P03535` → `D01-PRIMARY.P03538` |
| `TOP-059` | TOP-059 — Executar Fluxo Documental Notion | `D01-PRIMARY.P03577` → `D01-PRIMARY.P03580` |
| `TOP-060` | TOP-060 — Executar Skill Creator | `D01-PRIMARY.P03619` → `D01-PRIMARY.P03622` |
| `TOP-061` | TOP-061 — Gerador Skill Directory | `D01-PRIMARY.P03661` → `D01-PRIMARY.P03664` |
| `TOP-062` | TOP-062 — Plano Operacional Rastreável | `D01-PRIMARY.P03703` → `D01-PRIMARY.P03706` |
| `TOP-063` | TOP-063 — Paper Sprint Orchestrator | `D01-PRIMARY.P03745` → `D01-PRIMARY.P03748` |
| `TOP-064` | TOP-064 — Sprint Sheet | `D01-PRIMARY.P03787` → `D01-PRIMARY.P03790` |
| `TOP-065` | TOP-065 — Roadmap Sheet | `D01-PRIMARY.P03829` → `D01-PRIMARY.P03832` |
| `TOP-066` | TOP-066 — QR Intents | `D01-PRIMARY.P03871` → `D01-PRIMARY.P03874` |
| `TOP-067` | TOP-067 — Capture Reconcile | `D01-PRIMARY.P03913` → `D01-PRIMARY.P03916` |
| `TOP-068` | TOP-068 — MCP Builder (Anthropic) | `D01-PRIMARY.P03955` → `D01-PRIMARY.P03958` |
| `TOP-069` | TOP-069 — Skill Creator (Anthropic) | `D01-PRIMARY.P03997` → `D01-PRIMARY.P04000` |
| `TOP-070` | TOP-070 — Import Memory (Anthropic) | `D01-PRIMARY.P04039` → `D01-PRIMARY.P04042` |
| `TOP-071` | TOP-071 — Calendar Sprint Print System V1 | `D01-PRIMARY.P04081` → `D01-PRIMARY.P04084` |
| `TOP-072` | TOP-072 — Calendar Sprint Markers Package | `D01-PRIMARY.P04123` → `D01-PRIMARY.P04126` |
| `TOP-073` | TOP-073 — EXECUTAR 3PN + Good Path Standard | `D01-PRIMARY.P04165` → `D01-PRIMARY.P04168` |
| `TOP-074` | TOP-074 — Launch Control / Showroom Kit | `D01-PRIMARY.P04207` → `D01-PRIMARY.P04210` |
| `TOP-075` | TOP-075 — TRIGGER Mini Go Bookmark / Sprint Action Card | `D01-PRIMARY.P04249` → `D01-PRIMARY.P04252` |

## 6. Source-declared corrections

- **CORR-001 — Curso Cognitivo Estratégico**: `REMOVE_FROM_FUTURE_MASTER_INDEX`. Evidence: `D01-PRIMARY.P00804`, `D01-PRIMARY.P00869`.
- **CORR-002 — Bot / Plot**: `INTERPRET_AS_EXECUTAR_BLOG`. Evidence: `D01-PRIMARY.P00805`.

## 7. Agent retrieval procedure

For a TAP question, resolve the trace ID in `normalized_index.tap_schema.field_registry`, inspect `candidate_evidence_refs`, then read the referenced `D01-PRIMARY.P#####` blocks and their logical-unit neighborhood. For a corpus topic, resolve `TOP-###` directly. For provenance disputes, verify the exact source payload and SHA-256. Do not infer equivalence between the TAP and PRIMARY_CORPUS.

## 8. Integrity / reconstruction

- Original YAML is preserved as exact UTF-8 under `source_payloads.SRC-YAML-TAP-001.raw_utf8`.
- Original DOCX bytes are preserved in Base64 under `source_payloads.SRC-DOCX-PRIMARY-001.binary_base64`.
- Reconstructed files must match the SHA-256 values in the source registry.
- No source paragraph is deleted from the bundle; normalized units only reference source blocks.
