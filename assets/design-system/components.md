# Componentes — Edição HTML do Workbook (WB-H01–H17)

> Deliverable `D21-E01`. Estrutura/escopo canônicos em
> `registry/session_a/workbook_manual.yaml#html_edition.design_system`.
> Valores de token em `tokens.yaml` / `tokens.css` — extraídos literalmente de
> `docs/handoff/handoff-spec-onboarding-patterns.md` (SRC-07); impressão vem de SRC-04.
> **status: proposed** — pendente de aprovação humana (nenhum valor aqui é canônico).

Ordem de uso obrigatória (`density_priority`, `workbook_manual.yaml`):
**tabela → quadro → ficha → diagrama textual → lista → texto corrido.**
Use o formato mais denso que a informação permitir; texto corrido é o último recurso, nunca o padrão.

Regra transversal (`prohibitions`): sem jargão, sem estilo acadêmico ou de engenharia, sem
capítulos vazios, sem preencher lacuna com invenção — lacuna vira `Lacuna` (ver abaixo), nunca
texto genérico.

---

## Capa
**Mapeia:** `html_edition.cover`.
Campos: nome do ecossistema, título, versão, data da consolidação, situação documental, período coberto.

```html
<section class="ws-capa">
  <p class="ws-eyebrow">GOV-WORKBOOK-001</p>
  <h1 class="ws-titulo-capa">Workbook EXECUTAR</h1>
  <dl class="ws-capa-meta">
    <div><dt>Versão</dt><dd>1.1</dd></div>
    <div><dt>Consolidado em</dt><dd>2026-09-27</dd></div>
    <div><dt>Situação</dt><dd><span class="ws-chip ws-chip--proposed">proposed</span></dd></div>
    <div><dt>Período coberto</dt><dd>TBD</dd></div>
  </dl>
</section>
```
- Título: `var(--font-heading-lg)` peso 700 (`font-heading-lg` do handoff).
- Campo sem fonte confirmada: valor literal `TBD` (nunca inventar), sem estilo diferente do resto — a
  lacuna é sinalizada pelo conteúdo, não por decoração.

---

## Tabela
**Mapeia:** `WB-H03` (cadeia de valor), `WB-H05` (portfólio), `WB-H09` (processos), `WB-H11` (dados/fontes),
`WB-H13` (riscos), `WB-H16` (lacunas). Sempre que o registry já define `table: [...]` para o capítulo, a
tabela usa exatamente essas colunas, nessa ordem — não redesenhar o schema no HTML.

```html
<table class="ws-tabela">
  <caption>WB-H05 · Portfólio</caption>
  <thead>
    <tr><th>id</th><th>tipo</th><th>nome</th><th>área</th><th>objetivo</th><th>situação</th></tr>
  </thead>
  <tbody>
    <tr>
      <td class="ws-id">M2.1</td>
      <td>iniciativa</td>
      <td>Blog</td>
      <td>A08</td>
      <td>TBD</td>
      <td><span class="ws-chip ws-chip--proposed">proposed</span></td>
    </tr>
  </tbody>
</table>
```
- Cabeçalho: fundo `var(--color-surface-muted)`, texto `var(--color-text-secondary)` (mesmo par do
  handoff para popover/linha desabilitada).
- Linhas zebradas com `var(--color-surface-muted)` em `nth-child(even)`; divisor `1px solid var(--color-border)` —
  contraste mínimo AA mesmo em impressão P&B (a zebra é textura de borda, não só cor).
- Coluna de ID sempre com `var(--font-family-mono)` / `var(--font-mono)` (mesmo tratamento do chip OTP no handoff).
- `overflow-x: auto` no container para tabelas largas; nunca truncar coluna de ID.

---

## Quadro
**Mapeia:** uso geral em `WB-H01, H02, H04, H06, H07, H08, H10, H14, H15` — bloco de destaque para um
conceito, contrato ou resumo executivo que não é tabular nem uma ficha de processo.

```html
<div class="ws-quadro">
  <h3 class="ws-quadro-titulo">CTR-INTERFACE</h3>
  <p class="ws-quadro-corpo">Contrato de 10 campos aplicado a toda interface entre áreas (D01–D23).</p>
</div>
```
- `var(--radius-md)` (12px, mesmo raio de "botão/linha de lista/painel de dropdown" no handoff),
  `var(--shadow-modal)`, borda `1px solid var(--color-border)`, padding `var(--spacing-md)`.
- Título em `var(--font-heading-md)` peso 600, corpo em `var(--font-body)`.

---

## Ficha
**Mapeia:** `WB-H09.critical_process_sheet` — objetivo, entrada, pré-condições, passos, saída, critério
de aceite, responsável, evidência, exceções.

```html
<article class="ws-ficha">
  <header><span class="ws-id">D08-PRC-001</span><h3>Nome do processo</h3></header>
  <dl>
    <div><dt>Objetivo</dt><dd>TBD</dd></div>
    <div><dt>Entrada</dt><dd>TBD</dd></div>
    <div><dt>Pré-condições</dt><dd>TBD</dd></div>
    <div><dt>Passos</dt><dd><ol><li>TBD</li></ol></dd></div>
    <div><dt>Saída</dt><dd>TBD</dd></div>
    <div><dt>Critério de aceite</dt><dd>TBD</dd></div>
    <div><dt>Responsável</dt><dd>TBD</dd></div>
    <div><dt>Evidência</dt><dd>TBD</dd></div>
    <div><dt>Exceções</dt><dd>TBD</dd></div>
  </dl>
</article>
```
- Visualmente mais "pesada" que o quadro: `var(--shadow-modal)`, `var(--radius-md)`, cabeçalho com
  `border-bottom: 1px solid var(--color-border)`.
- Todo campo sem valor confirmado mostra `TBD` — nunca omitir o rótulo `dt`.

---

## Diagrama textual
**Mapeia:** árvores hierárquicas (ex.: a árvore de `docs/ARCHITECTURE.md#3`), usado quando a relação é
estrutural (pai/filho, fluxo) e uma tabela perderia a hierarquia.

```html
<pre class="ws-diagrama"><code>GOV-WORKBOOK-001
├── SESSÃO A — CONSULTA
│   └── SA-04 Domínios Canônicos D01–D23
└── SESSÃO B — PRODUÇÃO
    └── Foundation Doc SB-00…SB-11</code></pre>
```
- `var(--font-family-mono)`, `var(--font-body)`, `white-space: pre`, fundo `var(--color-surface-muted)`,
  `var(--radius-sm)`, sem quebra automática de linha (rolagem horizontal no container).

---

## Lista
**Mapeia:** enumerações simples sem relação estrutural nem campos suficientes para virar tabela
(ex.: `prohibitions`, `final_audit`).

```html
<ul class="ws-lista">
  <li>Cobertura</li>
  <li>Consistência</li>
  <li>Relações</li>
</ul>
```
- Marcador simples, `var(--spacing-sm)` entre itens, sem ícone decorativo (ícone só quando o registry
  define um significado para ele, nunca puramente estético).

---

## Chip de estado (`registry status`)
**Estados:** `proposed`, `active`, `deprecated`, `archived` (únicos valores válidos — `schema/workbook.schema.yaml#status`).
SRC-07 não define token de estado "pendente/aviso"; ver `derivacao_governanca` em `tokens.yaml`
para a justificativa de cada mapeamento (nenhuma cor nova, só reuso dos tokens do handoff).

```html
<span class="ws-chip ws-chip--proposed">proposed</span>
```
```css
.ws-chip { font: 500 var(--font-caption) var(--font-family); padding: 2px 8px; border-radius: var(--radius-sm); border: 1px solid; }
.ws-chip--proposed   { color: var(--ws-chip-proposed-texto);   background: var(--ws-chip-proposed-fundo);   border-color: var(--ws-chip-proposed-borda); }
.ws-chip--active     { color: var(--ws-chip-active-texto);     background: var(--ws-chip-active-fundo);     border-color: var(--ws-chip-active-borda); }
.ws-chip--deprecated { color: var(--ws-chip-deprecated-texto); background: var(--ws-chip-deprecated-fundo); border-color: var(--ws-chip-deprecated-borda); opacity: 0.7; }
.ws-chip--archived   { color: var(--ws-chip-archived-texto);   background: var(--ws-chip-archived-fundo);   border-color: var(--ws-chip-archived-borda); opacity: 0.55; }
```
- `deprecated`/`archived` reduzem opacidade seguindo a regra do handoff para `Button.Primary`
  desabilitado ("40% opacity, no pointer events") — aqui mais suave (0.7 / 0.55) para manter legibilidade
  em texto corrido.
- O texto do estado é sempre o rótulo literal (`proposed`, não um ícone) — obrigatório por
  `impressao.regra` em `tokens.yaml` (cor nunca é o único portador de significado).

## Chip de governança (`CNF` / `GAP` / `DEC` / `Gnn`)
Mesma mecânica do chip de estado, reusando tokens do handoff (`--ws-chip-conflito-*` = `color-accent-red`,
`--ws-chip-decisao-*` = `color-primary-blue` + `color-ai-suggestion-bg`, `--ws-chip-gate-*` =
`color-teams-badge`). O ID sempre visível dentro do chip, ex.
`<span class="ws-chip ws-chip--conflito">CNF-003</span>` — nunca o rótulo genérico sozinho
("conflito"), sempre com o ID rastreável.

---

## Acessibilidade
- Contraste mínimo AA (4.5:1 texto normal) para os pares texto/fundo herdados de SRC-07; `text-secondary`
  (`#6B6F76`) sobre `surface`/`surface-muted` já atende AA para texto normal — reconferir se o par mudar.
- Nenhum estado ou categoria depende só de cor — chip sempre carrega o rótulo textual.
- Tabelas usam `<th scope="col">` e `<caption>` com o ID do capítulo (`WB-Hnn`).
- Diagrama textual é `<pre><code>`, navegável por leitor de tela como texto, não como imagem.

## Impressão
- `@page { size: A4; margin: var(--print-margem-segura); }` (`tokens.css`; SRC-04, não SRC-07).
- `--shadow-modal` desligada em `@media print` — bordas (`--color-border`) sozinhas marcam os blocos.
- Cabeçalho/rodapé repetidos por página: `impressao.cabecalho_repetido` / `impressao.rodape_repetido`
  em `tokens.yaml`.
