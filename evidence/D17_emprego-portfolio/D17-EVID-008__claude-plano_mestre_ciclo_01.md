# PLANO MESTRE — Ciclo 01 Applied AI Europa

| Campo | Valor |
|---|---|
| ID | PLN-C01-ACAO |
| VERSION | 1.0 (18/09/2026) |
| AREA | Carreira · Portfólio · Capacitação · GTM |
| WORKFLOW | Value Sprints semanais (22) |
| OWNER | Leo (Project Owner) |
| STATUS | RELEASED — backlog no Linear, execução iniciada (S01) |
| Charter | PRJ-CAR-AI-EU-C01-2026-27 (não alterado) |
| Linear | projeto "Ciclo 01 — Applied AI Europa", issues EXE-191 a EXE-259, 8 milestones |

Legenda de origem: **[P]** dado pessoal · **[E]** evidência externa/auditoria · **[C]** cálculo · **[I]** inferência.

## 1. Entradas novas (18/09) e o que mudaram

| Dado [P] | Efeito no plano |
|---|---|
| Cidadania portuguesa (**hipótese** — texto recebido: "cursado português") | Direito de trabalho UE destrava PT/IE/ES/NL/FR/DE; UK continua exigindo visto. Confirmar em BL-E0-003. |
| Inglês fluente; FR/IT comunicação; ES básico | Inglês deixa de ser gap. FR ainda bloqueia J20/J21 (fluência nativa/profissional). |
| 0 anos em software; autodidata 18 meses | Vagas com ≥2 anos exigidos viram *target futuro*; cenário "sem 2 anos" do JSON passa a valer. |
| Experiência em negócios e gestão | Vira diferencial central: papéis AI + negócio têm o maior job-fit. |
| Psicologia incompleta (1,5 ano, Irlanda) | Vagas com graduação obrigatória (13/40) = excluir. Não declarar diploma. |
| 40 h/semana | Cenário EST-C: 836 h (vs. 627 h). Horas extras vão para candidaturas, entrevistas e um piloto real — não para mais frameworks. |
| Orçamento sem restrição | Custo sai do caminho crítico; o limite passa a ser tempo. FIN-04 ainda pede um teto formal (registro). |

## 2. Decisões registradas

| ID | Decisão | Justificativa | Origem |
|---|---|---|---|
| D-01 | Posicionamento: **AI Solutions Builder** (CV A, entrada imediata) + **Applied AI Engineer** (CV B, cresce com P01–P03). Agentic = especialidade. | Maiores job-fits sem blocker são papéis AI+negócio (J52 73, J56 73, J58 69, J57 65, J55 60); nenhuma vaga técnica aberta passou de 56. | [C]+[I] |
| D-02 | Python continua #1 (score 96,5 ≈ baseline 96). RAG #2. | Recalculado com matriz de 40 vagas e auditoria. | [C] |
| D-03 | Reranking deixa de ser nó próprio → experimento dentro do P02. | 1/40 menções explícitas. | [E]+[C] |
| D-04 | MCP/HITL saem do fim da cadeia → **empacotar** o que existe (P01) e portar para Python no P03. | Artefatos existem no Echo (parcial). | [E] |
| D-05 | Cloud = **Azure** (não AWS). | Stack escolhida no JSON; AI-103 é a credencial Azure vigente; AWS MLE score 41. | [C] |
| D-06 | CS50P (C01) em vez de Helsinki (C08). | Score 71 vs 68; Helsinki custa 100–140 h. Reavaliar Helsinki no Ciclo 02 se créditos ECTS ajudarem a retomar graduação. | [C]+[I] |
| D-07 | Autoria vira item de backlog explícito (README honesto, AUTHORSHIP.md, drills e gates ao vivo sem IA). | ~94% das linhas do Echo em commits do Claude; README ainda é do next-forge. | [E] |
| D-08 | Meta de candidaturas: 124 (vs. 120), com peso maior no fim do ciclo (10/semana S17–S22). | Capacidade de 40 h e cases prontos a partir de 15/01. | [C] |

## 3. Conflitos (CONFLITO) e bloqueios

| ID | Conflito | Impacto | Resolução |
|---|---|---|---|
| CF-01 | Notas do Prompt vs matriz de mercado (ex.: FastAPI 90 vs 61; reranking 83 vs 1/40) | Ordem de estudo | Resolvido: notas do prompt viram histórico; ranking recalculado (§4). |
| CF-02 | Macrofluxo da Estratégia vs datas do Charter | Datas de P02/editorial | Resolvido: Charter prevalece; Estratégia define composição semanal. |
| CF-03 | **Projeto "EXECUTAR — Plano integrado 14-09" no mesmo Linear** (27 fases, label "Semana Crítica", gate Google Play até 01/12) compete pelas mesmas 40 h | Se executado em paralelo, o Ciclo 01 perde capacidade (RSK-01) | **USER_ACTION_REQUIRED:** congelar esse lançamento até 18/02 (recomendação do JSON: "congelar novos produtos") ou declarar quantas horas ele consome. Não alterei esse projeto. |
| CF-04 | Charter FIN-04 exige teto financeiro; usuário declarou recursos ilimitados | Governança | Registrado como "sem restrição declarada em 18/09"; formalizar no checkpoint S02. |

## 4. Ranking de competências (score do Prompt, recalculado) [C]

Fórmula: Σ(nota 0–5 × peso) × 20 — demanda 30% (R + 0,5·D + 0,5·T normalizado) · gap pessoal 25% (gap 5 / parcial 2,5 / comprovada 0) · dependência 20% (nº de nós descendentes no DAG) · evidência 15% · valor/esforço 10%.

| # | Skill | Score | Baseline | Δ | Status [E] |
|---|---|---|---|---|---|
| 1 | Python | 96.5 | 96 | 0.5 | gap |
| 2 | RAG/retrieval | 72.1 | 89 | -16.9 | gap |
| 3 | Integração LLM | 67.8 | — | — | parcial |
| 4 | APIs/integrações | 65.6 | — | — | parcial |
| 5 | LangGraph/frameworks/estado | 64.8 | 81 | -16.2 | gap |
| 6 | Embeddings/vector DB (pgvector) | 61.6 | 89 | -27.4 | gap |
| 7 | FastAPI/Pydantic | 61.2 | 90 | -28.8 | gap |
| 8 | Agentes/tool calling | 59.2 | — | — | parcial |
| 9 | Docker | 55.9 | 68 | -12.1 | gap |
| 10 | Testes (pytest/vitest) | 53.4 | 90 | -36.6 | parcial |
| 11 | Fundamentos ML | 52.9 | 58 | -5.1 | gap |
| 12 | Evals + reranking | 49.5 | 83 | -33.5 | parcial |
| 13 | Observabilidade LLM | 48.6 | 75 | -26.4 | parcial |
| 14 | Cloud (Azure) | 46.4 | 73 | -26.6 | parcial |
| 15 | SQL/PostgreSQL | 41.4 | — | — | parcial |
| 16 | TypeScript/Node | 38.1 | 42 | -3.9 | parcial |
| 17 | MCP | 33.9 | 51 | -17.1 | parcial |
| 18 | Governança/guardrails | 21.8 | — | — | comprovada |
| 19 | CI/CD | 21.7 | — | — | comprovada |

Limitação: a nota de dependência penaliza nós terminais (evals, observabilidade, cloud), que ainda assim são exigidos para fechar cases; por isso a **sequência** segue o DAG, e o ranking decide **alocação de horas**.

## 5. DAG de dependências [I]

```
Python ─┬─> pytest ─┬─> FastAPI ─┬─> RAG ─> Evals+rerank ─┐
        │           │            └─> Docker ─> Azure ──────┤
        ├─> ML fundamentos ─> Evals                        ├─> CASE production-grade
        ├─> pgvector (+SQL) ─> RAG                         │
        └─> LangGraph <─ Agentes <─ LLM ─> Observabilidade ─┤
MCP <─ Agentes ; CI/CD, Governança, TypeScript ─────────────┘  (já parciais/comprovados: empacotar)
```

Baseline do prompt (Python → FastAPI/pytest → RAG → reranking/evals → LangGraph → MCP/HITL → observabilidade → Docker/cloud) **alterado**: observabilidade antecipada para outubro (P01), MCP/HITL empacotados em vez de aprendidos, ML em paralelo desde outubro.

## 6. Cursos (score do Prompt) [C]

| Curso | Score | Decisão |
|---|---|---|
| C02 FastAPI+pytest docs | 84.0 | Obrigatório |
| C03 RAG pgvector/hybrid/rerank | 81.0 | Obrigatório |
| C06 Langfuse | 77.0 | Obrigatório |
| C04 LangGraph Academy | 72.0 | Obrigatório (dez) |
| C01 CS50P | 71.0 | Escolhido (Python) |
| C08 Helsinki Python 5 ECTS | 68.0 | Alternativa; Ciclo 02 |
| C07 AI-103 Azure | 65.0 | Gate S19 |
| C05 Google MLCC | 63.0 | Obrigatório (ML) |
| C09 HF LLM Course | 46.0 | Consulta |
| C10 Rumos Academia | 42.0 | Não |
| C11 AWS MLE Associate | 41.0 | Não |

## 7. Job-fit das vagas (motor GTM) [C]

Hard blockers aplicados antes do score: direito de trabalho → idioma → graduação obrigatória → experiência mínima ≥ 2 anos.

| Vaga | Score | Decisão | Blockers |
|---|---|---|---|
| J52 Winners Group — AI & Automation Enthusiast | 73.0 | APLICAR SELETIVO + fechar gap | nenhum |
| J56 Madiff — AI Reverse Mentor (part-time, remoto) | 73.0 | APLICAR SELETIVO + fechar gap | nenhum |
| J58 YellowIpe — AI Product Manager (presencial) | 69.0 | APLICAR SELETIVO + fechar gap | nenhum |
| J57 BRAINR — Notion & Automation Engineer (remoto) | 65.0 | APLICAR SELETIVO + fechar gap | nenhum |
| J55 Integer Consulting — AI Transformation Specialist | 60.0 | APLICAR SELETIVO + fechar gap | nenhum |
| J47 Integer Consulting — AI Engineer (GenAI Specialist) | 56.0 | TARGET FUTURO | nenhum |
| J12 Orbit — Product Engineer | 56.0 | PROSPECTAR empresa (vaga expirada) | nenhum |
| J30 Ascending AI — Full-Stack AI Engineer (mid) | 54.0 | PROSPECTAR empresa (vaga expirada) | nenhum |
| J08 Kefron — Junior AI Engineer (Dublin) | 49.0 | PROSPECTAR empresa (vaga expirada) | nenhum |
| J33 Visor.ai — AI Engineer (1–3 anos) | 47.0 | TARGET FUTURO (1 ano exigido; expirada) | nenhum |
| J01 Kwalit — Full-Stack AI Developer (Node/Angular/Kafka) | 46.0 | TARGET FUTURO | nenhum |
| J19 Resilient Co — Full Stack Engineer (Python/FastAPI+React) | 46.0 | PROSPECTAR empresa (vaga expirada) | nenhum |
| J37 Dust — Software Engineer | 46.0 | PROSPECTAR empresa (vaga expirada) | nenhum |
| J51 Capgemini Invent — Agentic/GenAI Consultant | 55.0 | EXCLUIR (hard blocker) | Elegibilidade: 5 anos residência UK |
| J10 G-Research — Applied AI Engineer (Londres) | 54.0 | EXCLUIR (hard blocker) | Elegibilidade: UK: exige visto; patrocínio a confirmar |
| J21 Mirakl — Agent Builder freelance | 54.0 | EXCLUIR (hard blocker) | Idioma: FR exigido (compreensão ≠ fluência); Experiência mínima 3 anos |
| J39 Mistral — Applied AI Engineer Prototyping | 54.0 | TARGET FUTURO (blocker de experiência) | Experiência mínima 2 anos |
| J03 Eurotux — Junior AI Engineer | 47.0 | EXCLUIR (hard blocker) | Graduação obrigatória |
| J02 ITDS — Mid-Level AI Engineer | 47.0 | TARGET FUTURO (blocker de experiência) | Experiência mínima 2 anos |
| J09 Nelly — Junior AI Engineer | 47.0 | EXCLUIR (hard blocker) | Idioma: Alemão; Graduação obrigatória |
| J38 Mistral — Applied AI Fullstack (soberano) | 47.0 | EXCLUIR (hard blocker) | Elegibilidade: Cidadania francesa; Graduação obrigatória; Experiência mínima 2 anos |
| J36 360Learning — AI Engineer | 47.0 | TARGET FUTURO (blocker de experiência) | Experiência mínima 2 anos |
| J13 ML Reply — AI Application Engineer | 41.0 | EXCLUIR (hard blocker) | Idioma: Alemão C1; Graduação obrigatória |
| J31 ML6 — Medior AI Engineer | 41.0 | EXCLUIR (hard blocker) | Idioma: Holandês; Graduação obrigatória; Experiência mínima 2 anos |
| J35 ITDS — GenAI QA Automation (Mid) | 39.0 | EXCLUIR (hard blocker) | Experiência mínima 3 anos |

Nenhuma vaga ≥ 75 hoje. Leitura [I]: o funil técnico só abre depois de P01 (15/10) e P02 (30/11); até lá, o CV A capta o mercado AI+negócio.

## 8. Plano semanal (40 h; S12 = 20 h, S15 = 24 h, S16 = 32 h; total 836 h) [C]

| Semana | Início | Estudo | Construção | Candidatura | Entrevista | Editorial | Networking | GTM | Governança | Migração | Reserva | Total | Cand. alvo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S01 | 09-18 | 11 | 3 | 6 | 0 | 0 | 0 | 8 | 10 | 0 | 2 | 40.0 | 4 |
| S02 | 09-25 | 11 | 6 | 10 | 2 | 0 | 1 | 6 | 2 | 1 | 2 | 40.0 | 4 |
| S03 | 10-02 | 11 | 16 | 8 | 2 | 0 | 1 | 0 | 0 | 0 | 2 | 40.0 | 4 |
| S04 | 10-09 | 11 | 15 | 8 | 4 | 0 | 1 | 0 | 0 | 0 | 2 | 40.0 | 4 |
| S05 | 10-16 | 12 | 5 | 8 | 6 | 0 | 1 | 0 | 3 | 3 | 2 | 40.0 | 4 |
| S06 | 10-23 | 22 | 4 | 5 | 2 | 3 | 1 | 0 | 2 | 0 | 2 | 40.0 | 4 |
| S07 | 10-30 | 18 | 6 | 4 | 6 | 3 | 1 | 0 | 0 | 0 | 2 | 40.0 | 4 |
| S08 | 11-06 | 8 | 17 | 6 | 3 | 3 | 1 | 0 | 0 | 0 | 2 | 40.0 | 4 |
| S09 | 11-13 | 8 | 22 | 4 | 3 | 0 | 1 | 0 | 0 | 0 | 2 | 40.0 | 4 |
| S10 | 11-20 | 3 | 25 | 6 | 3 | 0 | 1 | 0 | 0 | 0 | 2 | 40.0 | 4 |
| S11 | 11-27 | 3 | 22 | 1 | 3 | 6 | 1 | 0 | 2 | 0 | 2 | 40.0 | 2 |
| S12 | 12-04 | 4 | 6 | 5 | 3 | 0 | 1 | 0 | 0 | 0 | 1 | 20.0 | 2 |
| S13 | 12-11 | 4 | 17 | 7 | 3 | 5 | 2 | 0 | 0 | 0 | 2 | 40.0 | 6 |
| S14 | 12-18 | 0 | 15 | 7 | 3 | 6 | 2 | 0 | 5 | 0 | 2 | 40.0 | 6 |
| S15 | 12-25 | 0 | 6 | 6 | 3 | 5 | 2 | 0 | 0 | 0 | 1 | 24.0 | 2 |
| S16 | 01-01 | 0 | 14 | 10 | 3 | 0 | 2 | 0 | 2 | 0 | 1 | 32.0 | 6 |
| S17 | 01-08 | 0 | 11 | 16 | 8 | 0 | 2 | 0 | 0 | 0 | 2 | 40.0 | 10 |
| S18 | 01-15 | 3 | 3 | 17 | 8 | 4 | 2 | 0 | 0 | 0 | 2 | 40.0 | 10 |
| S19 | 01-22 | 3 | 3 | 11 | 12 | 4 | 2 | 0 | 2 | 0 | 2 | 40.0 | 10 |
| S20 | 01-29 | 3 | 0 | 19 | 12 | 0 | 2 | 0 | 2 | 0 | 2 | 40.0 | 10 |
| S21 | 02-05 | 0 | 0 | 29 | 8 | 0 | 1 | 0 | 0 | 0 | 2 | 40.0 | 10 |
| S22 | 02-12 | 0 | 0 | 24 | 7 | 0 | 1 | 0 | 6 | 0 | 2 | 40.0 | 10 |

Horas de Candidatura incluem pesquisa, adaptação de CV e envio; nas semanas S17–S22 também absorvem processos seletivos. Validação automática: 69 itens, 0 erros de schema, 0 ciclos, dependências respeitam a ordem das semanas, soma = capacidade em todas as semanas.

## 9. Milestones (gates do Charter)

| Gate | Data | Critério | Issues |
|---|---|---|---|
| G1 Capability matrix | 30/09 | Matriz rastreável | EXE-191 ✅, 196 ✅, 192, 197, 202, 211, 203 |
| G2 P01 EXECUTAR | 15/10 | Release + demo + 20 cenários + alteração ao vivo | EXE-206, 212, 222, 229, 233 |
| G3 Python/FastAPI | 31/10 | API testada e containerizada; teste ao vivo | EXE-216, 224, 230 |
| G4 P02 RAG | 30/11 | Benchmark holdout + deploy + case | EXE-225, 232, 235, 237, 240, 242, 243, 244, 246 |
| G5 Editorial | 31/12 | E01–E04; E04 submetida | EXE-231, 245, 256, 238 |
| G6 Três cases | 15/01 | P01, P02, P03 publicados | EXE-247, 248, 254, 255, 257, 258, 259 |
| G7 Entrevista | 01/02 | Explicar e alterar cases sem IA | EXE-218, 252, 253 |
| G8 Decisão | 18/02 | Continuar/ajustar/Plano B | EXE-241 |

## 10. Métricas de progresso

- **Competência:** nº de gates ao vivo aprovados (meta 3: S04, S07, S20); drills sem IA/semana (meta 2).
- **Evidência:** cases com release + README + testes + demo (meta 3 até 15/01); cenários de falha versionados (meta 40).
- **Mercado:** candidaturas qualificadas (meta 124); taxa de resposta; entrevistas técnicas; motivo de rejeição por categoria.
- **Autoridade:** 4 peças; conversas técnicas iniciadas a partir delas (não likes).
- **Gates do funil:** 20 candidaturas/4 semanas sem contato → revisar CV/lista antes de outro curso; 3 entrevistas com o mesmo gap → treinar o gap.

## 11. Registro de evidências

| Evidência | Local |
|---|---|
| Auditoria dos repos | claude/CAPABILITY_MATRIX_CICLO_01.md |
| Backlog (17 campos, 69 itens) | claude/BACKLOG_CICLO_01.csv · Linear EXE-191…259 |
| Scores e cálculos | Este documento §4, §6, §7 (scripts reproduzíveis na sessão) |
| Vagas novas verificadas 18/09 | J55 Integer AI Transformation, J56 Madiff, J57 BRAINR, J58 YellowIpe AI PM; J01 e J47 reconfirmadas abertas |
| Pacote Sprint 01 | claude/PACOTE_SPRINT_01.md |
| Funil | claude/FUNIL_CANDIDATURAS.csv |

## 12. USER_ACTION_REQUIRED (lote único)

1. Confirmar cidadania portuguesa / direito de trabalho UE (EXE-192).
2. Decidir o projeto EXECUTAR 14-09 no Linear: congelar até 18/02 ou reservar horas (CF-03).
3. Preencher no CV A: anos, cargos e empresas de negócios; instituição na Irlanda (EXE-211).
4. Comprar passagem até 01/10 (EXE-195).
5. Enviar as 5 candidaturas piloto (EXE-219) — envio é seu.
6. Indicar um possível parceiro para o piloto real (EXE-236) — opcional até S08.

## 13. Próximo workflow preparado

Sprint S01 (18–24/09): EXE-197 README honesto → EXE-202/211 posicionamento e CV → EXE-194 CS50P → EXE-219 candidaturas. Review de quinta (24/09) fecha a semana com: competência + artefato + evidência + exposição.