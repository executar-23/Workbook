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

## Por que não vive no `registry/`

`registry/` guarda estrutura e relações (IDs, regex, referências) — não valores de design
literais (hex, px). Este pacote é o "implementation" referenciado pela estrutura: o registry
aponta para cá via `html_edition.design_system.assets_path`, não o contrário.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `tokens.yaml` | Fonte de verdade dos valores (cor, tipografia, espaçamento, raio, elevação, impressão) |
| `tokens.css` | Os mesmos valores como custom properties CSS (`--ws-*`), consumidos pelo HTML gerado |
| `components.md` | Um componente por formato de densidade + capa + chips de estado/governança, com markup, mapeamento para `WB-Hnn` e regras de acessibilidade/impressão |

## Status

`proposed` — nenhum valor de token é canônico até aprovação humana explícita (ver
`docs/AI_AGENT_PROTOCOL.md#modelo-epistêmico`: documento para em `PRE_PREENCHIDO`, aprovação é
ato humano). `epistemic_class: PROPOSED`, `source_refs: [SRC-04]` (SRC-04 define o pipeline e as
17 partes; não define cor/tipografia — por isso os valores literais aqui são propostos, não
derivados).

## Como usar

1. Ao gerar `WORKBOOK_INTEGRADO.html`, incluir `tokens.css` uma vez no `<head>`.
2. Para cada capítulo `WB-Hnn`, escolher o componente pelo campo já definido no registry
   (`table:`, `chain:`, `shape:`, `classes:` etc. em `workbook_manual.yaml#html_edition.parts`) —
   `components.md` traduz cada um para o formato de densidade correspondente.
3. Não redeclarar cor/tamanho soltos no HTML: sempre `var(--ws-*)`.
4. Rodar a auditoria final (`final_audit` no registry) incluindo conferência de contraste e de
   que nenhum estado depende só de cor (`components.md#acessibilidade`).

## Conflitos e lacunas

Nenhum conflito identificado no passo de inspeção (nenhum design system prévio existia no
repositório). Lacuna: paleta/tipografia não têm fonte além de SRC-04 (que não cobre visual) —
registrada como `status: proposed`, não como `GAP-nnn`, porque não bloqueia nenhuma entrega
existente; fica pendente de aprovação humana antes de qualquer publicação.
