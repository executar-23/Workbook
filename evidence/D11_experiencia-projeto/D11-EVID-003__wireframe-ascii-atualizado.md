Abaixo está o wireframe ASCII atualizado, incorporando Copiloto EXECUTAR, Solution Store, preenchimento dos cards, rotas e onboarding.

EXECUTAR — SOLUTION STORE / OFICINA
═══════════════════════════════════════════════════════════════════════
┌─────────────────────────────────────────────────────────────────────┐
│ EXECUTAR / OFICINA                     [Buscar...]   [Perfil]       │
│ [Discover] [Collections] [Learn] [Mapa Cognitivo]                  │
└─────────────────────────────────────────────────────────────────────┘
DISCOVER
┌─────────────────────────────────────────────────────────────────────┐
│ Encontre uma solução para o que precisa executar                    │
│                                                                     │
│ [🔎 Search________________] [Área ▼] [Tipo ▼] [Ordenar ▼]          │
│                                                                     │
│ For You │ Trending │ New │ Categories                              │
└─────────────────────────────────────────────────────────────────────┘
SOLUTION CARD
┌─────────────────────────────────────────────────────────────────────┐
│ [POSTER / VIDEO LOOP]                                               │
│                                                                     │
│ SKILL · PRODUCTIVITY                                                │
│ Copiloto EXECUTAR                                                   │
│                                                                     │
│ Copiloto operacional para executar a rotina diária sobre uma        │
│ fonte única de verdade.                                             │
│                                                                     │
│ [Operations] [Project Manager] [Entrepreneur]                       │
│                                                                     │
│ Organizar · Planejar · Documentar · Validar · Automatizar           │
│                                                                     │
│              [ Start ]             [ Download ]                     │
└─────────────────────────────────────────────────────────────────────┘
CARD SCHEMA
card
├── variant
├── solution_id
├── release_id
├── content
│   ├── eyebrow
│   ├── title
│   ├── short_description
│   ├── product_type
│   ├── primary_area
│   ├── professions[]
│   ├── tags[]
│   └── metadata[]
├── media
│   ├── poster
│   ├── video_loop
│   └── gif_fallback
└── actions
    ├── Start → onboarding
    └── Download → pacote
SOLUTION DETAIL — COPILOTO EXECUTAR
┌─────────────────────────────────────────────────────────────────────┐
│ [Icon] Copiloto EXECUTAR                     v1.0.0                 │
│ Skill Workflow                              [ START ] [ DOWNLOAD ]  │
├─────────────────────────────────────────────────────────────────────┤
│ [Overview] [Contents] [Examples / Try it] [Dependencies]           │
├─────────────────────────────────────────────────────────────────────┤
│ PROBLEMA                                                            │
│ Estado operacional fragmentado entre memória, planilhas e conversas │
│                                                                     │
│ PROCESSO                                                            │
│ ATIVAR → VALIDAR → RESOLVER → EXECUTAR → VERIFICAR                 │
│ → CALCULAR → REGISTRAR → EMITIR                                    │
│                                                                     │
│ PROGRESSO                                                           │
│ Fonte única → tarefa atual → DoD → evidência → próxima ação         │
├─────────────────────────────────────────────────────────────────────┤
│ COMANDOS                                                            │
│ /bomdia   /agora   /estado   /fechardia   /replanejamento          │
└─────────────────────────────────────────────────────────────────────┘
START → ONBOARDING
┌─────────────────────────────────────────────────────────────────────┐
│ 1 ●────2────3────4────5                                             │
│                                                                     │
│ O QUE É                                                             │
│ Copiloto operacional para conduzir execução diária.                 │
│                                                                     │
│ [Continuar →]                                                       │
└─────────────────────────────────────────────────────────────────────┘
01 O que é
      ↓
02 O que você precisa
      ↓
03 Como começar
      ↓
04 Exemplo
      ↓
05 Próxima ação
      ↓
EXECUTAR SOLUÇÃO
RESPOSTA OPERACIONAL DO COPILOTO
┌─────────────────────────────────────────────────────────────────────┐
│ [PROGRESSO] [SPRINT/C72] [GATE]                                    │
│                                                                     │
│ AGORA:            ID — ação                                         │
│ TEMPO:            duração                                           │
│ CONCLUI QUANDO:   DoD                                               │
│ EVIDÊNCIA:        prova esperada                                    │
│ PRÓXIMA:          uma ação                                          │
└─────────────────────────────────────────────────────────────────────┘
ROTEAMENTO / PRD DE PRODUÇÃO
SOURCE
  ↓
INGESTED
  ↓
CLASSIFIED
  ↓
SCHEMA_COMPLETE ───────────── G1
  ↓
BUNDLE_READY ──────────────── G2
  ↓
IN_EDITORIAL_PRODUCTION
  ↓
ASSETS_READY ──────────────── G3
  ↓
QA_READY ──────────────────── G4
  ↓
STORE_READY ───────────────── G5
  ↓
PUBLISHED ─────────────────── G6
RESPONSABILIDADE POR ROTA
D11  UX / wireframe / Design System
  ↓
D12  React / componentes / implementação
  ↓
D19  Solution Store / schema / assets / release
  ↓
D22  ADRs / decisões arquiteturais
  ↓
D23  Blueprints reutilizáveis
ARQUITETURA GERAL
Schema Unificado
      ↓
Mapa Cognitivo
      ↓
Problem → Concept → Evidence
      ↓
Quick Framework
      ↓
Quick Framework Block
      ↓
Solution Store
      ↓
Copiloto EXECUTAR
      ↓
Action
      ↓
Evidence / Result
      ↓
Metric / Learning
      └──────────────────────→ Schema

A regra central da implementação deve ser: o card é uma projeção do objeto SOLUTION; Start abre onboarding e Download permanece uma ação independente. O solution.yaml é a fonte da solução; card, listing, onboarding e assets são derivados dela.