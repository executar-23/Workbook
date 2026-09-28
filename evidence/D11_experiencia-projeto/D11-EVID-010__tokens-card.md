Adicione este bloco ao prompt anterior do Cloud. Ele transforma as duas referências em contrato visual + tokens + schema de conteúdo para os 10 cards.

# DESIGN CONTRACT — SOLUTION STORE CARDS
Use as imagens fornecidas como referências visuais. Não copie o conteúdo fictício; reproduza a linguagem visual usando dados reais das skills encontradas.
## 1. Design Tokens
```yaml
tokens:
  color:
    canvas: "#F2F3F4"
    surface: "#FFFFFF"
    surface_muted: "#F7F7F7"
    text_primary: "#111111"
    text_secondary: "#777777"
    text_muted: "#A0A0A0"
    border: "#D8D8D8"
    border_subtle: "#E8E8E8"
    accent_blue: "#48ADEB"
    accent_cyan: "#31BBDD"
    accent_green: "#72D99A"
    accent_lime: "#C4DC70"
    accent_orange: "#FFA52D"
    status_bg: "#F1F1F1"
  radius:
    xs: 8px
    sm: 12px
    md: 20px
    lg: 28px
    xl: 36px
  spacing:
    xs: 8px
    sm: 12px
    md: 16px
    lg: 24px
    xl: 32px
    xxl: 48px
  typography:
    family: "Inter, system-ui, sans-serif"
    eyebrow: 14px/500
    body: 16px/400
    body_small: 14px/400
    title: 28px/600
    display: 44px/600
  shadow:
    card: "0 8px 20px rgba(0,0,0,.12)"
    elevated: "0 14px 35px rgba(0,0,0,.14)"

⸻

2. CARD VARIANT — ONBOARDING / EXECUTION

Estrutura inspirada no primeiro card:

┌─────────────────────────────────────┐
│            ON BOARDING              │ ← faixa accent_blue
├─────────────────────────────────────┤
│ Título da Skill                     │
│ Descrição curta em 2 linhas         │
│                                     │
│ [avatars/agentes]      [STATUS]     │
├─────────────────────────────────────┤
│ 💬 8    🔗 4    📁 12      versão  │
└─────────────────────────────────────┘

Schema:

onboarding_card:
  eyebrow:
  title:
  description:
  agents: []
  status:
  interactions:
  dependencies:
  artifacts:
  version:
  updated_at:
  action:

Status possíveis:
Ready | Guided | Interactive | Beta | Production | In Progress

⸻

3. CARD VARIANT — SOLUTION DETAIL

Usar a segunda referência para cards mais comerciais/informativos.

┌─────────────────────────────────────┐
│ Nome da solução          [BADGE]    │
│ Outcome principal                   │
│ Descrição curta                     │
├─────────────────────────────────────┤
│ ✓ Benefício / capacidade 01         │
│   explicação curta                  │
│ ✓ Benefício / capacidade 02         │
│   explicação curta                  │
│ ✓ Benefício / capacidade 03         │
│ ✓ Entregável principal              │
├─────────────────────────────────────┤
│          START / EXECUTAR →         │
└─────────────────────────────────────┘
  Ideal para: [audience / JTBD]

Não utilizar preço se a skill não possuir modelo comercial.

Preencher automaticamente:

solution_card:
  name:
  badge:
  headline:
  short_description:
  capabilities:
    - title:
      description:
  deliverables: []
  ideal_for:
  time_to_value:
  capability_type:
  primary_cta:
  secondary_cta:

4. Regras

Para cada uma das 10 skills:

1. gerar onboarding_card;
2. gerar solution_card;
3. utilizar exclusivamente conteúdo derivado da skill real;
4. evitar Lorem Ipsum;
5. manter no máximo 4 capacidades principais no card;
6. mover conteúdo detalhado para /solutions/[slug];
7. START abre /solutions/[slug]/start;
8. cards devem funcionar em desktop, tablet e mobile;
9. hover: translateY(-2px) + aumento sutil de shadow;
10. foco de teclado sempre visível.

A Collection Page deve misturar os cards mantendo o mesmo sistema visual, espaçamento, radius e tipografia.