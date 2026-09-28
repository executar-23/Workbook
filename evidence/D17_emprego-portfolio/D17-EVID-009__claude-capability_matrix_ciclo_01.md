# CAPABILITY MATRIX — Ciclo 01 (OBJ-01 / ACC-01)

ID: CAP-C01-001 · VERSION 1.0 · 18/09/2026 · STATUS: VERIFIED (auditoria de código) · Fonte: 4 repos públicos Sas-Executar clonados + testes executados

Classificação: comprovada | parcial | gap | desconhecida. **Parcial** = artefato existe, mas domínio pessoal não demonstrado ou escopo incompleto.

| Skill | Status | Evidência verificada | Demanda (R/D/T em 40 vagas) |
|---|---|---|---|
| APIs/integrações | parcial | apps/api (Next route handlers) + packages/integrations 25 testes | 17/2/11 |
| Agentes/tool calling | parcial | packages/agent-runtime: tools, phases, write_policy, PRE_APPROVE (HITL); 33 testes passando | 17/2/10 |
| CI/CD | comprovada | 6 workflows; 8/8 testes de deployment-config passam; commit próprio 90d4aa9 (secret rotation) | 8/1/3 |
| Cloud (Azure) | parcial | Deploy Vercel via 6 workflows GitHub Actions; sem Azure/AWS | 12/11/4 |
| Docker | gap | Nenhum Dockerfile | 8/6/2 |
| Embeddings/vector DB (pgvector) | gap | Só utilitário de cosine similarity (packages/scanner); sem vector DB | 8/5/4 |
| Evals + reranking | parcial | 17 casos JSONL (golden/regression/adversarial) + graders de schema; sem eval de qualidade de resposta/retrieval | 9/2/9 |
| FastAPI/Pydantic | gap | Nenhum código FastAPI/Pydantic nos 4 repos | 4/0/3 |
| Fundamentos ML | gap | Sem notebook/treino; nenhuma evidência | 11/0/0 |
| Governança/guardrails | comprovada | 03-Exe-Governance: 50 commits próprios, 228 docs; RLS + authority-gate no Echo | 2/3/7 |
| Integração LLM | parcial | packages/ai com AI SDK + OpenAI router | 25/1/11 |
| LangGraph/frameworks/estado | gap | Sem estado persistido/retomável nem LangGraph | 15/10/5 |
| MCP | parcial | packages/mcp: server + 8 tools + audit de chamadas; 9 testes existem mas pulados sem DB | 2/1/4 |
| Observabilidade LLM | parcial | packages/observability: trace, ai-cost, metrics; 15 testes; sem plataforma de tracing LLM | 7/3/6 |
| Python | gap | ~65 linhas próprias em stubs (02-Exe-Maestro/orchestrator); 0 arquivos .py no Echo | 27/5/2 |
| RAG/retrieval | gap | Nenhum pipeline de retrieval nos repos | 15/3/8 |
| SQL/PostgreSQL | parcial | 8 migrations Prisma incl. enable_rls; maioria em commits do Claude | 7/0/3 |
| Testes (pytest/vitest) | parcial | 239 testes vitest passando em 13 pacotes TS (51 pulados por exigir DATABASE_URL); nenhum pytest | 5/0/6 |
| TypeScript/Node | parcial | ~35k linhas TS sobre template next-forge; ~94% das linhas em commits do Claude, ~2k em commits próprios | 10/5/3 |
| Negócios, gestão e stakeholders | comprovada (dado pessoal declarado) | Experiência em negócios/gestão informada em 18/09; empresas, cargos e datas: A DEFINIR | Comunicação/business value pesa 10% no job-fit |
| Inglês | comprovada (declarada) | Fluente — validar com walkthrough gravado (P01) | 11/40 exigem inglês fluente |
| Francês / italiano / espanhol | parcial (declarada) | FR/IT compreensão e comunicação; ES básico | FR exigido em J20/J21 → ainda blocker |

## Achados críticos da auditoria (evidência, não inferência)

1. **01-Executar-Echo é derivado do template vercel/next-forge** (1.270 commits de Hayden Bleasel, 2023-01 a 2026-03; licença MIT Vercel). O README ainda é o do next-forge.
2. **Trabalho adicionado de 09/09 a 13/09/2026:** 531 arquivos, ~35,6k linhas. Por autor de commit: ~35,1k linhas em commits "Claude" e ~2,0k em 12 commits próprios não-merge (principalmente CI/deploy, runbooks e CMS).
3. **Testes:** 239 passam em 13 pacotes; 51 são pulados porque exigem DATABASE_URL (inclui 100% dos testes de packages/mcp). Deploy-config: 8/8.
4. **Python:** ~65 linhas próprias (stubs de orquestrador, 26/08) + 1 script de 114 linhas gerado pelo Claude. Nenhum FastAPI, pytest, RAG, vector DB, Dockerfile ou LangGraph.
5. **Governança:** 03-Exe-Governance tem 50 commits 100% próprios e 228 documentos — é a evidência de autoria mais forte.

## Implicação (inferência)
RSK-04 (atribuição de competência) está **materializado**, não hipotético. O plano trata isso com: README honesto + AUTHORSHIP.md (BL-E1-005/006), drills sem IA (BL-E1-013), gates ao vivo gravados (BL-E1-015, BL-E3-006) e P02/P03 em Python escritos com assistência mínima. O posicionamento honesto e forte é: *"eu especifico, oriento e verifico sistemas de IA construídos com agentes — e consigo alterá-los sem eles"*.