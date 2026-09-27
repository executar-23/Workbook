# Arquitetura conceitual — Master Schema EXECUTAR v1.1

> Fonte canônica: `registry/`. Este texto explica; não redefine IDs nem relações.

## 1. Regra central
- **Sessão A — Consulta / Knowledge System**: o que o sistema **é e conhece** (`registry/session_a/`).
- **Sessão B — Produção / Execution System**: **como** o sistema executa (`registry/session_b/`).
- Objetos da Sessão B referenciam IDs da Sessão A em `refs_a` e nunca copiam conhecimento canônico (validado por `scripts/validate.py`).

Duas árvores independentes na Sessão A: **capacidades permanentes** (Axx → Dxx) e **portfólio** (P00 → Mxx). Produtos consomem capacidades; não as contêm.

## 2. Padrão transversal
Toda mudança relevante de contexto (seção SA, macroárea, domínio, conjunto documental) carrega, quando aplicável: capa · como ler/utilizar · resumo executivo (what/why/who/how) · IDs relacionados · fonte canônica. Definido uma vez em `master_index.yaml#transversal_pattern` e referenciado — nunca duplicado.

## 3. Árvore hierárquica (plain text)
```
GOV-WORKBOOK-001 — Sistema Integrado de Governança e Operação EXECUTAR
│
├── SESSÃO A — CONSULTA
│   ├── Master Index
│   │   ├── SA-00 Document Control
│   │   ├── SA-01 Workbook Executivo ── WB-P1 Manual de Governança (WB-P1-01…20)
│   │   │                             ── WB-P2 Playbook D01–D23 (CTR-PLAYBOOK + CTR-INTERFACE)
│   │   │                             ── WB-P3 Workbook de Execução → delega a SB-09
│   │   │                             ── Edição HTML WB-H01…H17
│   │   ├── SA-02 Arquitetura do Ecossistema
│   │   ├── SA-03 Macroáreas A00–A12
│   │   ├── SA-04 Domínios Canônicos D01–D23
│   │   ├── SA-05 Portfólio P00 / M0–M16
│   │   ├── SA-06 Control Plane
│   │   ├── SA-07 Governança Operacional (G00–G11, SRC, DEC, CNF, GAP)
│   │   ├── SA-08 Documentos Finais
│   │   ├── SA-09 Protocolo de Agentes IA
│   │   ├── SA-10 Alertas de Governança
│   │   ├── SA-11 Próximas Ações Críticas
│   │   └── SA-12 Corpus Detalhado D01–D23 (37 documentos)
│   │
│   ├── Árvore funcional
│   │   ECO-EXECUTAR
│   │   └── Axx Macroárea
│   │       └── Dxx Domínio (primary_area + supporting_areas)
│   │           └── Dxx.SDyy Subdomínio
│   │               └── Dxx-PRC-nnn Processo / Ciclo
│   │                   └── Dxx-Enn Entregável
│   │                       └── Dxx-DOC-ACR-nnn Artefato / Documento
│   │                           └── Dxx-DOC-ACR-nnn.secao.campo
│   │
│   ├── Árvore de portfólio
│   │   P00 Programa EXECUTAR
│   │   └── Mn / Mn.n Produto/Iniciativa ──consome──▶ Axx / Dxx
│   │       └── PRJ-Mn-nnn Projeto (instanciado na Sessão B)
│   │
│   └── Transversais: PM01–PM13 (ciclo de produto) · L0–L6 · matriz fractal
│
└── SESSÃO B — PRODUÇÃO
    ├── Foundation Doc SB-00…SB-11 (cada um com refs_a)
    │   00 Project Character · 01 Frameworks · 02 PRD · 03 Tech · 04 Editorial · 05 Pain
    │   06 Agent · 07 Operation · 08 Tasks and Issues · 09 Sprints/Roadmaps/Chronogram
    │   10 Control · 11 Complete System Mental Model
    ├── Fluxo: Ciclo → Objetivos → Capacidade → Roadmap → Prioridades → Backlog → Sprint → WIP
    │          → Entregáveis → Dependências → Risks/Issues → Gate → Resultado → KPI → Learning → Próximo Ciclo
    └── Objetos: CYC OBJ RDM BKL SPR TSK ISS PRJ RB ROT CRN TPL AGT CMD EDL WF SOP
```

## 4. Mapa Axx ↔ Dxx ↔ Portfólio ↔ Programa ↔ Produto ↔ Projeto

| Macroárea | Domínios (primário) | Apoia |
|---|---|---|
| A00 Governança Estratégia e Gestão | D01, D22 | D02, D03 |
| A01 Negócio e Go to Market | D13, D14, D15 | D16 |
| A02 Produto e Experiência | D10, D11 | D09 |
| A03 Handoff Produto → Engenharia | — | D10, D11, D12 (D12.SD01) |
| A04 Arquitetura Engenharia e Implementação | D12 | D05 |
| A05 Operações Plataforma e Segurança | D08 | D12, D20 |
| A06 Dados Pesquisa e Conhecimento | D05, D06, D09 | — |
| A07 Corporativo e Suporte | D02, D03, D04 | — |
| A08 Conteúdo Comunicação e Growth | D16 | D19 |
| A09 Execução e Planejamento do Trabalho | D07 | — |
| A10 Documentação e Governança do Conhecimento | D18, D21, D23 | D06, D22 |
| A11 Ferramentas IA e Ativos Reutilizáveis | D19, D20 | D23 |
| A12 Stakeholders e Ecossistema | D17 | — |

Portfólio `P00` → `M0…M16` (`portfolio.yaml`). Consumo confirmado: M0, M1 (com `capability_map`), M2, M2.1, M7.1; demais **TBD** (GAP-009). Projetos `PRJ-Mn-nnn`: nenhum confirmado.

Frentes do ecossistema (aplicação do Playbook): App→M1, Blog→M2, Copiloto-Operacional→M5 (DERIVED, GAP-001), Oficina→M3, Consultoria/Estúdio→M8, Comunidade/ONG→M11/M12, Marketplace→M9/M10, Afiliados→M13, Schola AI→M15, Emprego e Portfólio→M7.1; Infoprodutos/E-book, Curso Cognitivo.org, Creator Mídia, Estudos → **GAP-002…005** (nenhum ID criado).

## 5. Contratos
- **CTR-PLAYBOOK** (21 campos, mesma ordem para todo D01–D23 e frentes): identidade → missão → objetivo → escopo → stakeholders → entradas → processos → saídas → entregáveis → produtos/serviços → dados → sistemas → dependências → KPIs → riscos → governança → planejamento → capacidade → financeiro → evidências → status.
- **CTR-INTERFACE** (10 campos): RECEBE → DE → PROCESSA → PRODUZ → ENTREGA_PARA → GATE → SISTEMA_DE_REGISTRO → EVIDÊNCIA → SLA → OWNER.
- **Documento** (`documents.yaml`): metadados de SRC-03 + `sections` ou `record_schema`; campo = `Dxx-DOC-ACR-nnn.secao.campo` com o contrato epistêmico de `governance.yaml#epistemic_model`.

## 6. Documentos por domínio (37)
D01 DDE·TAP·MNE·MRE · D02 DGRC·MRC·PPT · D03 PFO·MFO · D04 PPC · D05 EPGD·DCM · D06 EGC·RMI · D07 PEX·PIM · D08 MOP·RUN · D09 PPE·DEB · D10 DRP·PRD · D11 EEP·DSI · D12 ETE · D13 DRM·GTM · D14 PCV · D15 PASC · D16 PEM · D17 PEP · D18 PCE · D19 PAC · D20 PPR · D21 PWB · D22 DRL · D23 PBL. Primeiro de cada domínio = MACRO.

## 7. Fontes
SRC-01 INDX.docx · SRC-02 Schema Workbook.md · SRC-03 Prompt Mestre de pré-preenchimento · SRC-04 Project Caracter.docx · SRC-05 Checklist de Product Management · SRC-06 PEM area.rtf. Conflitos: `governance.yaml#conflicts` (CNF-001…007).
