# PACOTE SPRINT 01 — 18/09 a 24/09/2026

ID: PKG-S01 · VERSION 1.0 · STATUS: PREPARED (aguarda validação e envio pelo usuário)
Hipótese de mercado da semana: *papéis que combinam IA aplicada e negócio (automação, AI PM, transformação) são o ponto de entrada mais curto para um perfil autodidata com experiência em gestão e sem diploma técnico.*
Evidência: job_fit.csv — as 5 maiores notas sem hard blocker são J52 (73), J56 (73), J58 (69), J57 (65), J55 (60). Nenhuma vaga Applied AI técnica aberta passou de 56.

---

## 1. Headline e value proposition (BL-E1-001) — rascunho

**Headline (LinkedIn/CV):**
AI Solutions Builder · Agentic systems, automation & governance · Business-to-engineering translator · Python / TypeScript · Lisbon / EU

**Value proposition (EN):**
I turn business problems into working AI systems. Over the last 18 months I taught myself to design and ship agentic software — an AI copilot platform with tool-calling, human-approval gates, MCP tools, evals and CI/CD — and I bring prior experience in business and management, so I can scope the problem with stakeholders, build the solution and explain its risks in plain language.

**Três provas (links):**
1. EXECUTAR platform — agent runtime with human-approval write policy, MCP server (8 tools), 239 passing tests, CI/CD (github.com/Sas-Executar/01-Executar-Echo) — *após BL-E1-005 (README honesto)*
2. Governance system — 228 documented decisions, requirement → control → evidence traceability (github.com/Sas-Executar/03-Exe-Governance)
3. Spec-first delivery — blueprints, agent contracts and development packets (github.com/Sas-Executar/04-exe-pre-Blueprint)

> Regra de honestidade (RSK-04): nunca escrever "built from scratch". Usar "designed, specified and shipped with AI coding agents; I review, test and modify the code".

---

## 2. CV A — AI Solutions & Automation (BL-E1-002) — esqueleto

```
[NOME] · Lisbon, Portugal (from Dec 2026) · [email] · [LinkedIn] · github.com/Sas-Executar
Work authorization: EU citizen (Portugal)   ← CONFIRMAR (BL-E0-003)
Languages: English (fluent) · Portuguese (native) · French & Italian (working) · Spanish (basic)

PROFILE
AI solutions builder combining [N] years in business and management with 18 months of
hands-on, self-taught AI engineering. I design agentic workflows with human approval,
governance and evaluation built in, and translate them for non-technical stakeholders.

CORE CAPABILITIES
Agentic workflows & tool calling · Human-in-the-loop controls · MCP · LLM evals ·
Process automation · Requirements & stakeholder management · Python (in progress,
CS50P) · TypeScript/Next.js · PostgreSQL (RLS) · CI/CD (GitHub Actions, Vercel)

SELECTED ENGINEERING PROJECTS
EXECUTAR — AI copilot platform (2026)
• Problem: [1 linha]  • Architecture: Next.js monorepo (next-forge base), agent runtime,
  MCP server, Postgres with row-level security
• Controls: write actions require human pre-approval; schema-validated agent output;
  adversarial eval set  • Evidence: 239 automated tests, CI/CD, [demo link após 15/10]
• Built with AI coding agents under my specification and review — see AUTHORSHIP.md
EXECUTAR Governance — decision & evidence system (2026) · 228 docs, traceability matrix

PROFESSIONAL EXPERIENCE (business & management)
[Cargo] · [Empresa] · [MM/AAAA–MM/AAAA]   ← A DEFINIR pelo usuário
• [resultado mensurável]  • [resultado mensurável]

EDUCATION
Psychology (BSc, incomplete — 1.5 years) · [Instituição], Ireland
CS50's Introduction to Programming with Python · Harvard (in progress, 2026)
```

Campos A DEFINIR (só você tem): nome/contatos, anos e cargos de negócios, instituição na Irlanda, resultados mensuráveis.

---

## 3. Mensagens de candidatura (BL-E1-017) — rascunhos em inglês

Todas as vagas foram verificadas como abertas em 18/09 no ITJobs. Reabrir o anúncio antes de enviar.

**J52 · Winners Group · AI & Automation Enthusiast (Lisboa, presencial)**
Atenção: €13–21k/ano, terça a sábado. Enviar só se aceitável.
> Hi — I'm applying for the AI & Automation role. I've spent the last 18 months building AI automations and an agentic copilot platform (tool-calling, human approval before any write action, automated tests). Before that I worked in business and management, so I start from the process and the people who use it. Happy to walk you through one automation end-to-end. Portfolio: github.com/Sas-Executar

**J56 · Madiff · AI Reverse Mentor (remoto, poucas horas/semana)**
Complementar, não substitui emprego principal. O anúncio cita faixa etária 24–30, o que pode ser ilegal na UE; avaliar.
> I teach and build with AI tools daily — Claude, agents, no-code builders and coding agents — and I've used them to ship a full AI platform as a non-traditional engineer. That's exactly the "learn by doing" path your leaders need. I can show a 20-minute session: from idea to validated prototype with an AI agent.

**J58 · YellowIpe · AI Product Manager (presencial 6 meses)**
> I combine product/business management experience with hands-on AI engineering: I specified and shipped an agentic platform (APIs, integrations, MCP tools, evals, governance) and I'm now building an evaluated RAG system. I can define KPIs for AI features and talk to engineers in their language. Happy to share the product spec and decision log behind EXECUTAR.

**J57 · BRAINR · Notion & Automation Engineer (remoto)**
> "Builder/doer with side projects" describes me: I've built AI automations and an agentic platform with Claude, Cursor-style coding agents and APIs, and I document everything as structured databases (228-document governance system). I'm strengthening Python scripting this quarter (CS50P). Portfolio: github.com/Sas-Executar

**J55 · Integer Consulting · AI Transformation Specialist**
Risco: perfil pede experiência em consultoria/AI; sua experiência de negócios pode contar — mencione-a com números.
> I bring business and management experience plus 18 months building AI systems myself — agent workflows with human approval, governance and evaluation. I can identify where AI creates value, prototype it, and explain the risks and controls to stakeholders. Governance evidence: github.com/Sas-Executar/03-Exe-Governance

---

## 4. Funil

Planilha: `claude/FUNIL_CANDIDATURAS.csv` (15 campos; 7 vagas pré-carregadas: 5 para candidatar agora + J47/J01 como alvos futuros).

## 5. Próxima ação desta semana (WIP = 1)

1. Você: confirmar cidadania (BL-E0-003) e preencher os campos A DEFINIR do CV.
2. Você: README honesto do Echo (BL-E1-005) — posso redigir se quiser.
3. Você: começar CS50P semana 0 (BL-E1-007), sem IA.
4. Você: enviar as 5 candidaturas e registrar no funil.
