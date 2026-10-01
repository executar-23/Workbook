# Design System — Edição HTML do Workbook (WB-H01–H17)

Deliverable `D21-E01` (`registry/session_a/architecture.yaml`, domínio `D21` Workbook,
subdomínio `D21.SD01` Edição HTML).

## O que é

Tokens e componentes para renderizar `WORKBOOK_INTEGRADO.html` — a edição HTML de 17 partes
(`WB-H01…WB-H17`) já especificada em
`registry/session_a/workbook_manual.yaml#html_edition`. Este pacote não define os 17 capítulos
nem o pipeline (isso já existe e é canônico); define **como eles se parecem**: cor, tipografia,
espaçamento e o markup dos seis formatos de densidade (`tabela → quadro → ficha → diagrama
textual → lista → texto corrido`).

## Fonte dos valores

Os valores de cor, tipografia, espaçamento, raio e sombra **não são inventados**: são extraídos
literalmente de `docs/handoff/handoff-spec-onboarding-patterns.md` (registrado como `SRC-07` em
`governance.yaml#sources`) — as tabelas "Design Tokens Used" desse handoff. Nomes de token
(`color-primary-blue`, `radius-md`, `shadow-modal` etc.) e valores (hex, px, rgba) reproduzem o
handoff 1:1 em `tokens.yaml` / `tokens.css`.

O handoff descreve um produto diferente (Outlook Mail/Calendar/Copilot, Linear OTP, Edge
onboarding) — ele não tem conceito de "estado de registro" (`proposed/active/deprecated/
archived`) nem de conflito/gap/decisão/gate, que são específicos do Workbook. Para esses
componentes de governança, `tokens.yaml#cor.derivacao_governanca` documenta explicitamente qual
token do handoff cada chip reaproveita e por quê — nenhuma cor nova fora do handoff foi
introduzida. A única lacuna real: o handoff não tem um token de "pendente/aviso", então
`chip_estado--proposed` fica neutro (`color-text-secondary` / `color-surface-muted`) até uma
decisão humana.

`impressao` (página A4, margem segura) não vem do handoff — SRC-07 é produto digital, não cobre
impressão. Esse grupo usa SRC-04 (que já especifica o pipeline HTML/PDF do Workbook) e continua
`epistemic_class: PROPOSED`.

## Por que não vive no `registry/`

`registry/` guarda estrutura e relações (IDs, regex, referências) — não valores de design
literais (hex, px). Este pacote é o "implementation" referenciado pela estrutura: o registry
aponta para cá via `html_edition.design_system.assets_path`, não o contrário.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `tokens.yaml` | Fonte de verdade dos valores (cor, tipografia, espaçamento, raio, elevação, impressão), com `epistemic_class`/`source_refs` por grupo |
| `tokens.css` | Os mesmos valores como custom properties CSS (`--color-*`, `--font-*`, `--spacing-*`, `--radius-*`, `--shadow-modal`, `--ws-chip-*`), consumidos pelo HTML gerado |
| `components.md` | Um componente por formato de densidade + capa + chips de estado/governança, com markup, mapeamento para `WB-Hnn` e regras de acessibilidade/impressão |

## Status

`proposed` — nenhum valor de token é canônico até aprovação humana explícita (ver
`docs/AI_AGENT_PROTOCOL.md#modelo-epistêmico`: documento para em `PRE_PREENCHIDO`, aprovação é
ato humano), mesmo sendo `epistemic_class: DIRECT` para os grupos extraídos de SRC-07 (fonte
existe e é literal; falta é aprovação, não evidência).

## Como usar

1. Ao gerar `WORKBOOK_INTEGRADO.html`, incluir `tokens.css` uma vez no `<head>`.
2. Para cada capítulo `WB-Hnn`, escolher o componente pelo campo já definido no registry
   (`table:`, `chain:`, `shape:`, `classes:` etc. em `workbook_manual.yaml#html_edition.parts`) —
   `components.md` traduz cada um para o formato de densidade correspondente.
3. Não redeclarar cor/tamanho soltos no HTML: sempre `var(--color-*)` / `var(--font-*)` / etc.
4. Rodar a auditoria final (`final_audit` no registry) incluindo conferência de contraste e de
   que nenhum estado depende só de cor (`components.md#acessibilidade`).

## Conflitos e lacunas

Nenhum conflito identificado no passo de inspeção (nenhum design system prévio existia no
repositório). Lacuna registrada: SRC-07 não tem token de "pendente/aviso" para
`chip_estado--proposed` (ver `tokens.yaml#derivacao_governanca.gap`) — fica neutro até decisão
humana; não é um `GAP-nnn` formal porque não bloqueia nenhuma entrega existente.

Conflito registrado depois (2026-10-01): `CNF-008` em `registry/session_a/governance.yaml` —
o ADR-DS-ROOT-MIGRATION-001 adota o design system do `executar-23/Risco-cognitivo-blog` como
default do ecossistema, com paleta e tipografia diferentes das de SRC-07. Nenhum token deste
pacote foi alterado; o apontador está em `DESIGN_SYSTEM.md` na raiz e a escolha da paleta fica
para decisão humana.
