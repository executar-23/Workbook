# Interface Analysis

> Documento gerado a partir de `Archive_2.zip`. Marcações: `[INCERTO]` = não determinável pela imagem; `[INFERIDO]` = dedução a partir do conjunto. Valores de cor marcados como "amostrado" foram lidos dos pixels das imagens (aproximados por compressão JPEG). Medidas em px são estimativas sobre a resolução do arquivo, salvo indicação contrária.

---

## 1. Contexto Geral

### 1.1 Natureza do conjunto

O ZIP **não representa um único produto nem um único fluxo de navegação**. É uma **coleção de referências de UI/UX** (moodboard) com telas de origens diferentes. `[INFERIDO]` O nome dos arquivos sugere uso como "referências de view" para um projeto (prefixos `View-`, `Viewcard-`, `view_comercial-`), mas o conteúdo real de vários arquivos **não corresponde ao nome** (ver seção 8, "Divergências nome × conteúdo").

| Grupo | Imagens (IDs) | O que é |
|---|---|---|
| Captura de app de IA (iPad) | 001, 017 | Modal "Add files" do ChatGPT sobre uma conversa |
| Cards de planos/preços | 002/003, 010/011 | Duas telas de pricing (2 planos e 3 planos) |
| Landing pages / vitrines marketing | 004/005, 008/009, 012/013, 018 | Templates de site SaaS/fintech/IA, hero, features, pricing |
| Wireframe low-fi | 014/015 | Landing page de imobiliária/decoração em escala de cinza, desktop + mobile |
| Componente de card de tarefa (Kanban) | 016 | Card "CRM Layout Draft" com etiqueta ON BOARDING |
| Widget de sistema (iOS) | 006/007 | "Privacy Report" do Safari |

### 1.2 Resumo objetivo

- **Tipo de aplicação:** mistura de páginas web de marketing (landing pages), componentes de UI (cards de plano, card de tarefa), widget de sistema iOS e um screenshot de app de chat.
- **Objetivo provável:** servir de **repertório visual** para desenhar landing pages comerciais, telas de preços, cards de tarefa e onboarding. `[INFERIDO]`
- **Domínio:** SaaS, produtividade/gestão de tarefas, fintech, IA corporativa, imobiliário/decoração (wireframe).
- **Perfil provável do usuário do conjunto:** designer/desenvolvedor reunindo referências para gerar código ou wireframes. `[INFERIDO]` (reforçado pelo screenshot 001, cuja conversa de fundo fala em "Wireframe Contract").
- **Dispositivos/formatos aparentes:** desktop (002, 004, 008, 010, 012, 014 esquerda, 016, 018), iPad (001, 006), iPhone mockup (dentro de 004, 008, 018), mobile wireframe (014 direita).
- **Padrões visuais recorrentes:** cards brancos com cantos muito arredondados e sombra suave; fundos cinza-claro ou gradientes pastel azul; tipografia sans-serif geométrica; CTAs em pílula; mockups de iPhone; uso de gradiente como destaque (bordas e botões).
- **Quantidade total:** **18 arquivos de imagem** → **10 imagens distintas** (8 pares/duplicatas byte a byte idênticas, comprovadas por MD5).
- **Numeração:** os arquivos vão de `01` a `11`; **não existe arquivo `09`**.

---

## 2. Índice das Telas

| ID | Arquivo | Nome inferido da tela | Descrição curta | Duplicata de |
|---|---|---|---|---|
| 001 | `01_View-group.PNG` | ChatGPT iPad — modal "Add files" | Modal de seleção de arquivos recentes sobre conversa | — |
| 002 | `02_Viewcard-open.JPG` | Pricing — Personal vs Business | Dois cards de plano ($25 e $50/mês) com CTA em gradiente | — |
| 003 | `02_Viewcard-open 2.JPG` | Pricing — Personal vs Business (cópia) | Idêntica a 002 | 002 |
| 004 | `03_View_inforgraficacomercialsotre.JPG` | Pôster "100+ Premium Templates" — Nearo | Divulgação de template + hero "Get early access" + features | — |
| 005 | `03_View_inforgraficacomercialsotre 2.JPG` | Pôster Nearo (cópia) | Idêntica a 004 | 004 |
| 006 | `04_View-onbarding-tutorial.jpg` | Widget Privacy Report (Safari) | Card com escudo e 3 métricas de 30 dias | — |
| 007 | `04_View-onbarding-tutorial 2.jpg` | Privacy Report (cópia) | Idêntica a 006 | 006 |
| 008 | `05_view_comercial-landing-midia.JPG` | Seção "Powerful features to boost productivity" | Grade 2×2 de features com mockups | — |
| 009 | `05_view_comercial-landing-midia 2.JPG` | Seção features (cópia) | Idêntica a 008 | 008 |
| 010 | `06_view-move-select-card.JPG` | Pricing 3 planos — Nanodose/Microdose/Customdose | Seção de preços com plano central destacado | — |
| 011 | `06_view-move-select-card 2.JPG` | Pricing 3 planos (cópia) | Idêntica a 010 | 010 |
| 012 | `07_view-store-select.JPG` | Seção "We've orchestrated Intelligence." | Hero + 4 cards numerados (01, 02 expandido, 03, 04) | — |
| 013 | `07_view-store-select 2.JPG` | Seção Intelligence (cópia) | Idêntica a 012 | 012 |
| 014 | `08_viewlandingpage.JPG` | Wireframe landing page (desktop + mobile) | Wireframe cinza de imobiliária/decoração | — |
| 015 | `08_viewlandingpage 2.JPG` | Wireframe landing page (cópia) | Idêntica a 014 | 014 |
| 016 | `10_viewcard-.JPG` | Card de tarefa Kanban — CRM Layout Draft | Card com etiqueta ON BOARDING, avatares, status e contadores | — |
| 017 | `10_viewcard-group.JPG.PNG` | ChatGPT iPad — modal "Add files" (cópia) | Idêntica a 001 (mesmo hash, apesar do nome/extensão diferentes) | 001 |
| 018 | `11_view comcercial full pront.jpeg` | Landing page fintech "Payno" (página completa em 2 colunas) | Hero, features, pricing 3 planos, depoimentos, CTA final | — |

**Prova de duplicidade (MD5):**

| Hash MD5 | Arquivos | Dimensões |
|---|---|---|
| `d73524d9…` | 01_View-group.PNG = 10_viewcard-group.JPG.PNG | 1640×2360 |
| `f2116777…` | 02_Viewcard-open.JPG = 02_Viewcard-open 2.JPG | 1200×1025 |
| `8fb4bd2b…` | 03_… = 03_… 2 | 1000×1500 |
| `043a9adb…` | 04_… = 04_… 2 | 1170×916 |
| `785cdcbe…` | 05_… = 05_… 2 | 736×981 |
| `3d0aca8f…` | 06_… = 06_… 2 | 735×491 |
| `c6222f25…` | 07_… = 07_… 2 | 454×381 |
| `fef933a6…` | 08_… = 08_… 2 | 236×419 |
| `cd74d429…` | 10_viewcard-.JPG (única) | 1199×1176 |
| `a651a612…` | 11_view comcercial full pront.jpeg (única) | 1199×1499 |

---

## 3. Arquitetura Geral da Interface

Como as imagens são referências independentes, esta seção descreve os **padrões recorrentes entre elas**, não uma arquitetura de um só app.

### 3.1 Navegação
- **Navbar de landing page** (004, 018): logo à esquerda; em 018 há links centrais em pílula (`Home`, `Watch`, `About Us`, `FAQ`, `Blog`) e CTA `Download App` à direita; em 004 apenas logo `Nearo` e botão `TEMLIS`.
- **Sidebar de app** (001, ao fundo): lista `Library`, `Projects`, `Plugins`, `Scheduled`, `Remote`, `Explore`, seção `Pinned`, seção `Recents`.
- **Tabs/segmentos** (018 pricing e "Download App / Get Started"): toggle `Monthly / Yearly`.
- Sem breadcrumbs, sem paginação numerada. Carrosséis com setas/dots aparecem no wireframe 014.

### 3.2 Header
- 004: barra transparente sobre hero azul (logo + botão branco em pílula).
- 018: barra em pílula translúcida com links, sobre hero de céu.
- 001: header do app com ícone de menu, botão de compor e "…" (parcialmente escurecido pelo overlay).

### 3.3 Sidebar
- Apenas em 001/017 (ChatGPT). Fundo cinza-claro, itens com ícone + texto, lupa no topo, botão flutuante `Chat` azul e ícone de engrenagem no rodapé.

### 3.4 Conteúdo principal
- Landing pages: hero → features → prova social/pricing → CTA.
- Cards de plano lado a lado (002, 010, 018).
- Grades de cards de feature (004, 008, 018, 012).

### 3.5 Modais e overlays
- **Modal "Add files"** (001/017): folha branca com cantos grandes sobre fundo esmaecido, botão fechar (X) circular à esquerda, título central, botão "…" circular à direita.
- Nenhum outro modal identificado.

### 3.6 Formulários
- 004: campo de e-mail + botão `JOIN WAITLIST` integrados numa única pílula.
- 018: mini-formulário de pagamento (`We're paying for`, `Pay with` Card/Bank Account, número do cartão, validade, CVC, botão `Get Start`), e formulário de transferência (`Send Money`).
- 001: campo de busca `Search library` sobreposto.

### 3.7 Botões e ações
- CTA primário em gradiente (002), CTA primário sólido azul-violeta (010 plano central), CTA escuro em pílula (012 `Explore More`, 018 botões), CTA branco em pílula (004, 018 navbar), botões secundários com contorno (010).
- Links textuais azuis (`Show More` em 006).

### 3.8 Tipografia e hierarquia visual
- Sans-serif geométrica/grotesca em quase todas (Lato-like em 002 `[INFERIDO]`; Inter/Helvetica-like em 004, 012, 018).
- Serif itálica de contraste para destaque de marca em 010 (`dose`) e serif de display em 008 (título "Powerful features…").
- Numeração grande em cinza claro (012: `01.`, `03.`, `04.`).

### 3.9 Componentes reutilizáveis
Card de plano (002, 010, 018), card de feature com mockup (004, 008, 018), mockup de iPhone (004, 008, 018), pílula/badge (002 `POPULAR`, 010 `BEST VALUE TO PRICE`, 004 `COMING SOON`, 012 `MISSION`), lista de features com check (002, 010, 018), CTA em pílula, avatares sobrepostos (008, 016, 018).

### 3.10 Estados da interface
- Selecionado/destacado: card central de 010 (borda em gradiente + faixa superior); card expandido 02 em 012; card "Pro Plan" em 018.
- Overlay aberto: 001.
- Item destacado por sobreposição: 008 (card `Wireframe Homepage` sobre `User Testing`).
- Ativo em toggle: `Monthly` em 018 `[INCERTO]`.
- Nenhum estado de loading, erro ou vazio explícito em imagens completas.

---

## 4. Fluxo entre Telas

**Não há fluxo demonstrado entre as imagens**: são referências independentes. Nenhuma tela mostra o resultado de uma ação da anterior. Relações abaixo são apenas **temáticas** `[INFERIDO]`.

```
Referências de pricing:
[002 Pricing 2 planos] ── mesma família ──> [010 Pricing 3 planos] ──> [018 Payno (seção pricing)]

Referências de landing/features:
[004 Nearo hero+features] ──> [008 Powerful features] ──> [012 Intelligence] ──> [018 Payno página completa]
                                        └── mesma origem visual (mockups Temlis/Nearo) [INFERIDO]

Referências de componentes:
[016 Card Kanban ON BOARDING]   (isolado; alimenta a ideia de board/lista de tarefas mostrada em 004/008)

Referências estruturais:
[014 Wireframe landing]  ──> serve de "esqueleto" para o padrão de 018 e 004 [INFERIDO]

Ferramentas/contexto:
[001 ChatGPT Add files]  ──> contexto de uso: enviar estas imagens/arquivos a um agente [INFERIDO]
[006 Privacy Report]     (isolado; widget iOS, sem relação de navegação)
```

Fluxo interno demonstrado apenas em 001: `[conversa]` → botão `+` (barra inferior, visível sob o overlay) → `[modal Add files]` → `Upload files` ou seleção em `Recent` `[INFERIDO]`.
---

## 5. Telas

> Convenção para duplicatas: cada arquivo tem sua própria seção. Quando o arquivo é **byte a byte idêntico** (MD5 igual) a outro, a seção declara a diferença exata (**nenhuma**) e remete ao ID canônico para o wireframe e componentes, para evitar repetir conteúdo idêntico.

---

### Tela 001 — ChatGPT iPad: modal "Add files"

**Arquivo:** `01_View-group.PNG` · **ID:** 001 · **Resolução:** 1640×2360 (retrato, iPad) · **Duplicata:** 017

#### Objetivo da tela
Permitir ao usuário anexar arquivos à conversa: `Upload files` (do dispositivo) ou escolher entre arquivos `Recent` da biblioteca.

#### Contexto
Screenshot de app de chat de IA (ChatGPT) em iPad com modal aberto sobre uma conversa. A conversa ao fundo discute "Wireframe Contract" / "Wireframe → React Contract". É a única imagem do conjunto que é screenshot de produto real em uso, e não referência de design.

#### Estrutura visual
De cima para baixo:
1. **Status bar** iPadOS: `03:14 Mon 28 Sep` à esquerda; Wi-Fi e bateria `67%` à direita.
2. **Sidebar esquerda** (~40% da largura, fundo cinza-claro esmaecido): marca `ChatGPT` + ícone de lupa; menu; seção `Pinned`; seção `Recents`; rodapé com botão `Chat` azul e engrenagem.
3. **Coluna de conversa** (direita, esmaecida): header com ícone de menu, ícone de compor, "…"; mensagem do assistente com texto, dois blocos de código "Plain text" com ícone de copiar, texto de fechamento, ícones de ação (copiar, feedback, compartilhar, mais) e chip `Sources`; barra de entrada `Ask ChatGPT` com `+`, microfone e botão de voz azul.
4. **Overlay escurecido/esmaecido** cobrindo tudo.
5. **Modal centralizado** (~65% da largura, cantos ~32 px): header com X circular, título `Add files`, botão "…" circular; linha `Upload files` com ícone de upload; divisor; rótulo `Recent`; grade de cards 3 colunas; barra `Search library` flutuante sobre a última linha.

#### Componentes identificados
| Componente | Posição | Conteúdo | Estado | Interação aparente |
|---|---|---|---|---|
| Status bar | topo | hora, data, wifi, 67% | default | — |
| Sidebar | esquerda | navegação + histórico | esmaecida por overlay | itens clicáveis (fora do overlay) |
| Item de recente destacado | Recents, 1º item | `Stack Microso…` | destacado (fundo cinza) `[INFERIDO: conversa ativa]` | selecionar conversa |
| Botão `Chat` | canto inferior esquerdo | ícone lápis + texto | azul sólido | nova conversa `[INFERIDO]` |
| Bloco de código | conversa | `Plain text` + ícone copiar; 1º bloco mostra `Wireframe Specification…` | default | copiar |
| Modal `Add files` | centro | ver abaixo | aberto | fechar (X), menu (…) |
| Linha `Upload files` | topo do modal | ícone upload + texto | default | abre seletor do sistema `[INFERIDO]` |
| Card de arquivo (nota) | grade `Recent` | nome truncado + ícone de nota azul (inferior esq.) + círculo de seleção (sup. dir.) | não selecionado | toque seleciona (checkbox circular) |
| Card skeleton | linha 2, coluna 3 | 1 barra cinza + 1 círculo cinza | loading | — |
| Cards de imagem | linha 3 | miniaturas de screenshots de UI | parcialmente cortados | selecionar |
| Barra `Search library` | base do modal | ícone lupa + placeholder | default | campo de busca |

#### Conteúdo textual
- Status: `03:14 Mon 28 Sep`, `67%`
- Sidebar: `ChatGPT`; `Library`, `Projects`, `Plugins`, `Scheduled`, `Remote`, `Explore`; `Pinned`: `Converte…`, `Estratég…`, `Equacao…`, `Termos t…`; `Recents`: `Stack Microso…`, `ARCH-BLOG`, `Explicação do…`, `Transposição…`, `Gerar ADR E I…`, `E-mails do No…`, `Busca de documentos cognitivos`, `Transcrição de texto`, `Estrutura e resumo executivo`, `Gerar infográfico minimalista`, `Analisar imagens e gerar CSV`, `Conta logada no Notion`; botão `Chat`.
- Conversa (fragmentos legíveis, parcialmente encobertos): `A própria Figma está levando essa arquitetura para agentes: o Code C[…]` / `[…]ct conecta componentes visuais diretamente aos [TEXTO ILEGÍVEL] reais do repositório e fornece essas referências aos agentes de IA para melhorar a implementação.` · chip `Figma Developers +1` · `Para o seu projeto, eu melhoraria uma coisa` · `Em vez de aceitar qualquer .txt livre, criaria um Wireframe Contract oficial:` · `Plain text` · `Wireframe Specification` (truncado) · fragmentos `[…]nte livre.`, `[…]nada às`, `[…]e é transformar`, `[…]e, permitindo`, `[…]ando apenas` · `Eu consideraria esse Wireframe → React Contract uma parte formal da arquitetura do projeto, não apenas uma convenção de prompt.` · chip `Sources` · placeholder `Ask ChatGPT`.
- Modal: `Add files`, `Upload files`, `Recent`, cards: `AIKB-0003__con-ceito-blog-full-st…` (×3, incluindo um na linha 2 col. 1 e outro na linha 2 col. 2 — ver wireframe), `Aikb-0003(1)`, `Aikb-0003`, placeholder de loading, `Search library`.

#### Elementos interativos
- X (fechar) — Ação: fechar modal `[INFERIDO]`
- "…" (menu do modal) — Ação: [INCERTO]
- `Upload files` — abre seletor de arquivos `[INFERIDO]`
- Cards de arquivo com radio/checkbox circular — seleção múltipla `[INFERIDO]`
- Campo `Search library` — filtra biblioteca `[INFERIDO]`
- Elementos da sidebar e barra de entrada existem, mas estão sob o overlay.

#### Estado da interface
Modal aberto; conteúdo de fundo esmaecido (desfoque + branco translúcido); nenhum arquivo selecionado; um card em estado loading (skeleton); lista de recentes com rolagem (3ª linha cortada).

#### Wireframe textual
```
┌────────────────────────────────────────────────────────────────────────────┐
│ 03:14 Mon 28 Sep                                            ≈  67% ▮▮▮▯    │
├──────────────────────────────┬─────────────────────────────────────────────┤
│ ChatGPT                  🔍  │  ☰                             ✎   …        │
│                              │  A própria Figma está levando essa...        │
│ ▤ Library                    │  ... [chip: Figma Developers +1]             │
│ ▭ Projects                   │  Para o seu projeto, eu melhoraria uma coisa │
│ ◎ Plugins                    │  Em vez de aceitar qualquer .txt livre,...   │
│ ◷ Scheduled       ╔══════════════════════════════════════════╗             │
│ ▭ Remote          ║ (X)           Add files            (…)  ║             │
│ ⊞ Explore         ║                                          ║             │
│                   ║ ⇪ Upload files                           ║             │
│ Pinned            ║ ──────────────────────────────────────── ║             │
│  Converte…        ║ Recent                                   ║             │
│  Estratég…        ║ ┌────────────┐┌────────────┐┌──────────┐ ║             │
│  Equacao…         ║ │AIKB-0003__ ││AIKB-0003__ ││Aikb-0003 │ ║             │
│  Termos t…        ║ │con-ceito.. ││con-ceito.. ││(1)       │ ║             │
│                   ║ │  ▣      ○  ││  ▣      ○  ││  ▣     ○ │ ║             │
│ Recents           ║ └────────────┘└────────────┘└──────────┘ ║             │
│ [Stack Microso…]  ║ ┌────────────┐┌────────────┐┌──────────┐ ║             │
│  ARCH-BLOG        ║ │Aikb-0003   ││AIKB-0003__ ││ ▬▬▬▬     │ ║             │
│  Explicação do…   ║ │  ▣      ○  ││  ▣      ○  ││ ●(skel.) │ ║             │
│  Transposição…    ║ └────────────┘└────────────┘└──────────┘ ║             │
│  Gerar ADR E I…   ║ ┌────────────┐┌────────────┐┌──────────┐ ║             │
│  E-mails do No…   ║ │(thumb UI)  ││(thumb UI)  ││(thumb MS)│ ║             │
│  Busca de docs…   ║ ╞════════════════════════════════════════╡ ║             │
│  Transcrição…     ║ │ 🔍 Search library                      │ ║             │
│  Estrutura e…     ║ ╚══════════════════════════════════════════╝             │
│  Gerar infográf…  │  [Plain text  ⧉] Wireframe Specification...              │
│  Analisar imag…   │  Eu consideraria esse Wireframe → React Contract...      │
│ [✎ Chat]      ⚙   │  ⧉ 👍 ⤴ …   (Sources)                                   │
│                   │  ( + )  Ask ChatGPT                  🎤  (◉ voz)         │
└───────────────────┴──────────────────────────────────────────────────────────┘
```
> Nota: a grade real do modal tem 3 colunas × 3 linhas visíveis; a linha 2 inclui `Aikb-0003` (col. 1), `AIKB-0003__con-ceito-blog-full-st…` (col. 2) e o skeleton (col. 3). A ordem exata dos 3 primeiros cards da linha 1 é: `AIKB-0003__con-ceito-blog-full-st…`, `AIKB-0003__con-ceito-blog-full-st…`, `Aikb-0003(1)`.

#### Relações com outras telas
```
001
 ├── X (fechar)          -> conversa sem modal (não presente no ZIP) [INFERIDO]
 ├── Upload files        -> seletor de arquivos do iPadOS (não presente) [INFERIDO]
 └── cards de imagem     -> anexo de screenshots à conversa [INFERIDO]
```

#### Observações
- Todos os arquivos "recentes" de texto exibem o mesmo ícone (nota azul), sem miniatura.
- O card de nome truncado com quebra "con-/ceito" indica que o nome usa hífen duro dentro de `conceito`.
- Layout: modal sobrepõe a sidebar e a conversa; o botão `Chat` flutuante da sidebar e a barra de entrada ficam visíveis abaixo do overlay.

---

### Tela 002 — Pricing: Personal Plan vs Business Plan

**Arquivo:** `02_Viewcard-open.JPG` · **ID:** 002 · **Resolução:** 1200×1025 (paisagem) · **Duplicata:** 003

#### Objetivo da tela
Comparar dois planos de assinatura de uma ferramenta de finanças e levar o usuário a assinar.

#### Contexto
Componente/section de pricing sobre fundo cinza-claro com padrão de pontos. Relaciona-se por tema com 010 e com a seção de pricing de 018.

#### Estrutura visual
- Fundo `#F2F3F5` (amostrado) com trama de pontos sutil.
- Dois cards brancos lado a lado, mesma altura (~600 px), cantos ~32 px, borda fina em gradiente (esq.: verde-lima → laranja; dir.: ciano → verde-água) e sombra suave.
- Cada card: título + (no esquerdo) badge; preço grande; subtítulo; divisor colorido; 4 itens de feature com ícone de check tricolor, título e descrição em 2 linhas.
- **Aba de CTA** colada sob cada card: faixa arredondada com gradiente contendo texto branco + seta. A aba tem largura igual à do card e "escorrega" por baixo (~70 px de altura).
- Abaixo de cada aba: nota `*Ideal for:` em cinza pequeno.

#### Componentes identificados
| Componente | Posição | Conteúdo | Estado | Interação |
|---|---|---|---|---|
| Card Personal | esquerda | ver texto | default (destacado por badge) | — |
| Badge `POPULAR` | canto sup. dir. do card esquerdo | texto branco caixa-alta em pílula escura (`#292E32` amostrado) | estático | — |
| Preço | abaixo do título | `$25` grande + `/ month` pequeno | — | — |
| Lista de features | corpo | 4 itens (check + título + descrição) | — | — |
| CTA `Subscribe this plan →` | aba inferior | texto branco, gradiente lima→laranja (`#C1D576`→`#F79935` amostrado) | default | assinar plano `[INFERIDO]` |
| Card Business | direita | idem | default | — |
| CTA Business | aba inferior | gradiente azul→ciano→verde (`#3CBEF0`→`#2FF6F9`→`#7EE4B2` amostrado) | default | assinar plano |
| Nota `*Ideal for:` | sob cada aba | asterisco + rótulo preto, texto cinza | — | — |

#### Conteúdo textual
**Card esquerdo:** `Personal Plan` · `POPULAR` · `$25` `/ month` · `All-In-One Solution for Business Finances` ·
1. `Multi-user access` — `Allow multiple users to access and manage the finances`
2. `Detailed cash flow analysis` — `Analyze your cash flow in detail to make informed decisions`
3. `Automated expense tracking` — `Automatically track and categorize expenses to save time`
4. `Dedicated account manager` — `Get personalized support with a dedicated account manager`
· `Subscribe this plan →` · `*Ideal for:` `Individuals looking to manage their personal finances with essential tools.`

**Card direito:** `Business Plan` · `$50` `/ month` · `All-In-One Solution for Business Finances` · mesmas 4 features e descrições · `Subscribe this plan →` · `*Ideal for:` `Enterprice looking to manage their personal finances with essential tools.`

> Texto preservado como está: `Enterprice` (grafia original) e "personal finances" no card Business (incoerente com o plano). Os dois planos têm **lista de features idêntica**; só mudam nome, preço, cor e nota.

#### Elementos interativos
- `Subscribe this plan →` (×2) — Ação: [INCERTO] (assinatura/checkout `[INFERIDO]`)
- Nenhum outro controle.

#### Estado da interface
Default. Plano `Personal` sinalizado como popular (estado de destaque), sem seleção explícita.

#### Wireframe textual
```
┌───────────────────────────────────────────────────────────────────────────┐
│ (fundo cinza-claro pontilhado)                                            │
│                                                                           │
│  ┌──────────────────────────────┐   ┌──────────────────────────────┐      │
│  │ Personal Plan     [POPULAR]  │   │ Business Plan                │      │
│  │                              │   │                              │      │
│  │ $25 / month                  │   │ $50 / month                  │      │
│  │ All-In-One Solution for      │   │ All-In-One Solution for      │      │
│  │ Business Finances            │   │ Business Finances            │      │
│  │ ──────────── (lima→laranja)  │   │ ──────────── (ciano)         │      │
│  │ ✓ Multi-user access          │   │ ✓ Multi-user access          │      │
│  │   Allow multiple users...    │   │   Allow multiple users...    │      │
│  │ ✓ Detailed cash flow analysis│   │ ✓ Detailed cash flow analysis│      │
│  │   Analyze your cash flow...  │   │   Analyze your cash flow...  │      │
│  │ ✓ Automated expense tracking │   │ ✓ Automated expense tracking │      │
│  │   Automatically track...     │   │   Automatically track...     │      │
│  │ ✓ Dedicated account manager  │   │ ✓ Dedicated account manager  │      │
│  │   Get personalized support...│   │   Get personalized support...│      │
│  ├──────────────────────────────┤   ├──────────────────────────────┤      │
│  │ ▓▓ Subscribe this plan  →  ▓▓│   │ ▓▓ Subscribe this plan  →  ▓▓│      │
│  └──────────────────────────────┘   └──────────────────────────────┘      │
│  *Ideal for: Individuals looking…    *Ideal for: Enterprice looking…      │
└───────────────────────────────────────────────────────────────────────────┘
```

#### Relações com outras telas
```
002
 ├── Subscribe this plan (Personal) -> checkout [INCERTO / não presente]
 └── Subscribe this plan (Business) -> checkout [INCERTO / não presente]
```

#### Observações
- A aba de CTA fica **fora** do card branco e tem o mesmo raio do card, criando efeito de "card com base colorida".
- Ícone de check: tricolor (azul, verde-limão, laranja) `[INFERIDO: gradiente dentro do glifo]`.
- Divisor sob o subtítulo usa a mesma paleta de gradiente da borda/CTA de cada plano.

---

### Tela 003 — Pricing Personal vs Business (cópia)

**Arquivo:** `02_Viewcard-open 2.JPG` · **ID:** 003

**Relação:** cópia exata da Tela **002** (MD5 `f2116777…`, 1200×1025).
**Diferença observada:** **nenhuma** (mesmo conteúdo, mesmas dimensões, mesmos bytes). O sufixo " 2" indica duplicação de arquivo, não uma variação de estado.
**Wireframe, componentes, textos e interações:** idênticos aos de 002.

---

### Tela 004 — Pôster "100+ Premium Templates" — Nearo Coming Soon

**Arquivo:** `03_View_inforgraficacomercialsotre.JPG` · **ID:** 004 · **Resolução:** 1000×1500 (retrato, proporção 2:3) · **Duplicata:** 005

#### Objetivo da tela
Peça promocional (cover/Pinterest-style) de um template de site "Coming Soon" com lista de espera, mostrando preview da página.

#### Contexto
Combina uma **capa de divulgação** (topo) com o **preview de uma landing page** (corpo). É uma referência de hero + countdown + seção de features. Mockups internos compartilham identidade com 008/009.

#### Estrutura visual
1. **Faixa de capa** (fundo azul-acinzentado `#ABC0D1` amostrado, ~330 px): título em 2 linhas — `100+ PREMIUM` (texto preto grande) e `TEMPLATES` (branco sobre pílula preta) + cartão branco arredondado com três logos (Webflow, Framer, Figma) à direita; abaixo, subtítulo em preto.
2. **Moldura branca** com o site: hero em bloco azul com gradiente radial (claro no centro `#86C4ED` na base, amostrado), cantos ~20 px.
   - Navbar dentro do hero: logo `Nearo` à esquerda, botão branco pílula `TEMLIS` à direita.
   - Badge `COMING SOON`.
   - H1 centralizado `Get early access` (branco, 2 linhas).
   - Parágrafo centralizado.
   - Campo de e-mail + botão `JOIN WAITLIST` numa pílula translúcida.
   - **Mockup de iPhone** centralizado sobrepondo a base do hero (tela "My tasks").
   - **Countdown** em 4 caixas translúcidas na base do hero, sobre o iPhone.
3. **Seção 2** (fundo cinza `#F7F7F7`): título centralizado `Features designed for your success.`, subtítulo, e grade de cards 2 colunas (2 visíveis + 2 cortados).

#### Componentes identificados
| Componente | Posição | Conteúdo | Estado | Interação |
|---|---|---|---|---|
| Pílula de título | capa | `TEMPLATES` branco em preto | estático | — |
| Cartão de logos | capa, dir. | Webflow, Framer, Figma | estático | — |
| Navbar | topo do hero | logo Nearo + botão `TEMLIS` | default | link/CTA `[INCERTO]` |
| Badge | hero | `COMING SOON` | estático | — |
| Campo de e-mail | hero | placeholder `Your email address` | vazio | digitar |
| Botão `JOIN WAITLIST` | dentro do campo | texto pequeno caixa-alta, fundo branco | default | enviar e-mail `[INFERIDO]` |
| Mockup iPhone | hero centro | app "My tasks" | estático | — |
| Countdown | base do hero | 4 caixas: `200 DAYS`, `4 HOURS`, `56 MINUTES`, `4 SECONDS` separadas por `:` | dinâmico `[INFERIDO]` | — |
| Cards de feature | seção 2 | ver texto | default | — |

#### Conteúdo textual
- Capa: `100+ PREMIUM` · `TEMPLATES` · `Nearo - Comign Soon Website` (grafia original: "Comign")
- Hero: `Nearo` · `TEMLIS` · `COMING SOON` · `Get early access` · `We're getting close. Sign up to get early access to Naero and start building your viral waitlist.` (nota: "Naero" ≠ "Nearo", inconsistência de origem) · `Your email address` · `JOIN WAITLIST`
- iPhone: `9:41` · `My tasks` · `TOP PRIORITY` · tarefa `Final Design Review` / `Produtis App` / tag `High Priority` / data `Feb 22` · tarefa `Landing page` / `Temlis` / `High Priority` / `Feb 24` · `DUE TODAY`
- Countdown: `200` `DAYS` : `4` `HOURS` : `56` `MINUTES` : `4` `SECONDS`
- Seção 2: `Features designed for your success.` · `Explore the features designed to keep you organized and on track.`
  - Card 1: (visual: pilha de tarefas `User Testing` → `Wireframe Homepage` / `Temlis` / `High Priority` / `Feb 19`, `Feb 20`) · `Task Management` · `Stay on top of everything, from to-dos to long-term projects.`
  - Card 2: (visual: iPhone `Good morning, Rona 🔥` + chip `Work this week 12:09:07`) · `Time Tracking` · `Understand where your time goes and maximize every minute.`
  - Cards 3 e 4: cortados no limite inferior; apenas topo dos mockups visível. Texto: [TEXTO ILEGÍVEL]

#### Elementos interativos
- Campo de e-mail (input)
- `JOIN WAITLIST` — Ação: cadastrar na lista de espera `[INFERIDO]`
- `TEMLIS` (botão navbar) — Ação: [INCERTO]
- Countdown não é interativo.

#### Estado da interface
Default, pré-lançamento (estado "coming soon"). Campo de e-mail vazio. Nenhum erro/sucesso visível.

#### Wireframe textual
```
┌────────────────────────────────────────────────────────────────────┐
│ (fundo azul-acinzentado)                                           │
│  100+ PREMIUM                                                      │
│  ┌───────────────┐  ┌────────────────────┐                         │
│  │  TEMPLATES    │  │ [W]  [F]  [Figma]  │                         │
│  └───────────────┘  └────────────────────┘                         │
│  Nearo - Comign Soon Website                                       │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ ┌──────────────────────────────────────────────────────────┐ │  │
│  │ │ (hero azul gradiente)                                    │ │  │
│  │ │ ◻ Nearo                                     ( TEMLIS )   │ │  │
│  │ │                     ( COMING SOON )                      │ │  │
│  │ │                    Get early access                      │ │  │
│  │ │        We're getting close. Sign up to get early…        │ │  │
│  │ │        ┌──────────────────────────────────────┐          │ │  │
│  │ │        │ Your email address     (JOIN WAITLIST)│         │ │  │
│  │ │        └──────────────────────────────────────┘          │ │  │
│  │ │                 ┌──────────────┐                         │ │  │
│  │ │                 │ 9:41   ◉     │                         │ │  │
│  │ │                 │ My tasks     │                         │ │  │
│  │ │                 │ TOP PRIORITY │                         │ │  │
│  │ │  ┌─────┐ : ┌─────┐ : ┌─────┐ : ┌─────┐                    │ │  │
│  │ │  │ 200 │   │  4  │   │ 56  │   │  4  │                    │ │  │
│  │ │  │DAYS │   │HOURS│   │MINS │   │SECS │                    │ │  │
│  │ │  └─────┘   └─────┘   └─────┘   └─────┘                    │ │  │
│  │ └──────────────────────────────────────────────────────────┘ │  │
│  │              Features designed                               │  │
│  │              for your success.                               │  │
│  │      Explore the features designed to keep you…              │  │
│  │  ┌──────────────────────┐  ┌──────────────────────┐          │  │
│  │  │ [pilha de tarefas]   │  │ [iPhone + chip 12:09]│          │  │
│  │  │ Task Management      │  │ Time Tracking        │          │  │
│  │  │ Stay on top of…      │  │ Understand where…    │          │  │
│  │  └──────────────────────┘  └──────────────────────┘          │  │
│  │  ┌ (card 3 cortado) ┐      ┌ (card 4 cortado) ┐              │  │
└──┴──────────────────────────────────────────────────────────────┴──┘
```

#### Relações com outras telas
```
004
 ├── seção de features (cards Task Management / Time Tracking) -> desenvolvida em 008 [INFERIDO]
 └── mockup iPhone "My tasks" -> reaparece em 008 (Seamless Collaboration) [INFERIDO]
```

#### Observações
- A imagem é uma **composição de divulgação**, não uma tela pura; a capa (título + logos) não faz parte do site.
- O countdown se sobrepõe ao iPhone com vidro fosco (backdrop-blur) `[INFERIDO]`.
- Cards 3 e 4 da seção de features são cortados pelo enquadramento.

---

### Tela 005 — Pôster Nearo (cópia)

**Arquivo:** `03_View_inforgraficacomercialsotre 2.JPG` · **ID:** 005

**Relação:** cópia exata da Tela **004** (MD5 `8fb4bd2b…`, 1000×1500).
**Diferença observada:** **nenhuma**. Wireframe, componentes, textos e interações idênticos aos de 004.

---

### Tela 006 — Widget "Privacy Report" (Safari)

**Arquivo:** `04_View-onbarding-tutorial.jpg` · **ID:** 006 · **Resolução:** 1170×916 (paisagem) · **Duplicata:** 007

#### Objetivo da tela
Mostrar ao usuário um resumo dos últimos 30 dias de bloqueio de rastreadores pelo Safari.

#### Contexto
Widget/cartão da tela inicial do Safari (iOS/iPadOS). **Divergência:** o nome do arquivo diz "onboarding-tutorial", mas o conteúdo é um relatório de privacidade, sem passos de tutorial. `[INFERIDO]` Provavelmente usado como referência de "card informativo com métricas".

#### Estrutura visual
- Fundo `#F2F1F6` (amostrado) com sombra lateral direita (borda do screenshot).
- Título de seção `Privacy Report` (negrito, ~34 px) no canto superior esquerdo.
- **Cartão branco** largo (cantos ~40 px) dividido em **duas colunas**:
  - **Esquerda:** ícone de escudo verde (metade preenchida) no topo; texto `Safari prevents trackers from profiling you.` ao centro vertical; link `Show More` no rodapé.
  - **Direita:** rótulo `Last 30 days` e **3 tiles cinza** (`#F2F2F2` aprox.) empilhados, cantos ~20 px, cada um com rótulo cinza e valor preto em negrito.

#### Componentes identificados
| Componente | Posição | Conteúdo | Estado | Interação |
|---|---|---|---|---|
| Título de seção | topo esq. | `Privacy Report` | — | — |
| Ícone de escudo | cartão, sup. esq. | escudo verde (`#65C466` amostrado), metade sólida/metade contorno | — | — |
| Texto de resumo | cartão, esq. centro | frase | — | — |
| Link `Show More` | cartão, inf. esq. | azul iOS | default | expandir/abrir relatório completo `[INFERIDO]` |
| Rótulo de período | col. dir., topo | `Last 30 days` (cinza) | — | — |
| Tile métrica 1 | col. dir. | `Trackers prevented from profiling you` / `54` | — | — |
| Tile métrica 2 | col. dir. | `Websites that contacted trackers` / `66%` | — | — |
| Tile métrica 3 | col. dir. (maior) | `Most contacted tracker` / `google.com was prevented from profiling you across 29 websites` | — | — |

#### Conteúdo textual
`Privacy Report` · `Safari prevents trackers from profiling you.` · `Show More` · `Last 30 days` · `Trackers prevented from profiling you` `54` · `Websites that contacted trackers` `66%` · `Most contacted tracker` `google.com was prevented from profiling you across 29 websites`

#### Elementos interativos
- `Show More` — Ação: [INCERTO] (expandir/ver detalhes `[INFERIDO]`)
- Tiles: possivelmente tocáveis — Ação: [INCERTO]

#### Estado da interface
Default, com dados preenchidos (estado "com dados"). Sem estados de erro/vazio.

#### Wireframe textual
```
┌──────────────────────────────────────────────────────────────────────┐
│ Privacy Report                                                       │
│ ┌──────────────────────────────────────────────────────────────────┐ │
│ │  ◖█ shield verde                       Last 30 days              │ │
│ │                                        ┌────────────────────────┐│ │
│ │                                        │ Trackers prevented from││ │
│ │                                        │ profiling you          ││ │
│ │                                        │ **54**                 ││ │
│ │                                        └────────────────────────┘│ │
│ │  Safari prevents trackers              ┌────────────────────────┐│ │
│ │  from profiling you.                   │ Websites that contacted││ │
│ │                                        │ trackers   **66%**     ││ │
│ │                                        └────────────────────────┘│ │
│ │                                        ┌────────────────────────┐│ │
│ │                                        │ Most contacted tracker ││ │
│ │                                        │ **google.com was       ││ │
│ │  Show More                             │ prevented from         ││ │
│ │                                        │ profiling you across   ││ │
│ │                                        │ 29 websites**          ││ │
│ │                                        └────────────────────────┘│ │
│ └──────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────┘
```

#### Relações com outras telas
```
006
 └── link "Show More" -> relatório detalhado (não presente) [INFERIDO]
```

#### Observações
- Hierarquia: rótulo cinza pequeno → valor preto negrito grande.
- Tiles têm gradiente sutil (mais claro à esquerda, mais escuro à direita) `[INFERIDO]` por sombra lateral do screenshot.

---

### Tela 007 — Privacy Report (cópia)

**Arquivo:** `04_View-onbarding-tutorial 2.jpg` · **ID:** 007

**Relação:** cópia exata da Tela **006** (MD5 `043a9adb…`, 1170×916).
**Diferença observada:** **nenhuma**. Todo o conteúdo idêntico a 006.

---

### Tela 008 — Seção "Powerful features to boost productivity"

**Arquivo:** `05_view_comercial-landing-midia.JPG` · **ID:** 008 · **Resolução:** 736×981 (retrato) · **Duplicata:** 009

#### Objetivo da tela
Apresentar 4 funcionalidades de um app de tarefas (gestão, agendamento, colaboração, notificações) com mockups.

#### Contexto
Seção de features de landing page (mesmo universo visual de 004: Temlis/Rona, tarefas "Wireframe Homepage", iPhone "My tasks"). Está dentro de uma moldura branca sobre fundo cinza-azulado `#89929B` (amostrado).

#### Estrutura visual
- Fundo externo cinza-azulado; moldura branca com borda cinza-clara (`#E1E5E8`).
- Cabeçalho da seção centralizado: título serifado em 2 linhas + subtítulo em 2 linhas.
- **Grade 2×2** de cards `#ECF0F3` (amostrado), cantos ~20 px. Cada card: área de mockup (topo, ~65%) e legenda (baixo): **nome da feature em cor escura + descrição em cinza** na mesma frase/parágrafo centralizado.

#### Componentes identificados
| Componente | Posição | Conteúdo | Estado | Interação |
|---|---|---|---|---|
| Título serifado | topo | `Powerful features to boost productivity` | — | — |
| Card 1 (Simple Task Management) | linha 1, col. 1 | pilha de cartões de tarefa | card "Wireframe Homepage" em destaque sobre "User Testing" (checked, esmaecido) e "Normal" | — |
| Card 2 (Smart Scheduling) | linha 1, col. 2 | iPhone `Good morning, Rona 🔥` + chip flutuante `Work this week 12:09:07` | — | — |
| Card 3 (Seamless Collaboration) | linha 2, col. 1 | iPhone `My tasks` + pílula com 4 avatares e ícone de troféu | — | — |
| Card 4 (Real-Time Notifications) | linha 2, col. 2 | card `Goals / Rona Zepri` com 3 métricas | — | — |

#### Conteúdo textual
- `Powerful features to boost productivity`
- `Designed to simplify your workflow, our powerful features help you manage tasks effortlessly and efficiently.`
- **Card 1** (mockup): `User Testing` `Feb 19` · `Wireframe Homepage` `Feb 20` · `Temlis` · `High Priority` · `Normal`. Legenda: `Simple Task Management` `Effortlessly create, organize, and prioritize tasks with an intuitive interface.`
- **Card 2** (mockup): `Thu, 20 February` · `Good morning, Rona 🔥` · `Work this week` `12:09:07` · `Apps Projects` · métricas `Completed 10`, `Overdue 0`, `Due 4` · `Top priority` lista `Final Design Review`, `Landing page`, `Wireframe Homepage`. Legenda: `Smart Scheduling` `Set due dates, recurring tasks, and get automated reminders to stay on track.`
- **Card 3** (mockup): `9:41` · `My tasks` · `TOP PRIORITY` · `Final Design Review` / `Produtis App` / `High Priority` · `Landing page` / `Temlis` / `High Priority` · `DUE TODAY` · `Wireframe Homepage` / `Produtis App`. Legenda: `Seamless Collaboration` `Assign tasks, share progress, and communicate effortlessly with your team.`
- **Card 4** (mockup): `Goals` `Rona Zepri` · `Task 10/[TEXTO ILEGÍVEL]` · `Time 10h/[TEXTO ILEGÍVEL]` · `Projects 5/[TEXTO ILEGÍVEL]`. Legenda: `Real-Time Notifications` `Stay informed with instant alerts on task updates, deadlines, and team activities.`

#### Elementos interativos
Nenhum controle explícito. Mockups são ilustrativos. Cards possivelmente sem interação (seção estática).

#### Estado da interface
Default (seção estática de marketing).

#### Wireframe textual
```
┌──────────────────────────────────────────────────────────────┐
│ (fundo cinza-azulado)                                        │
│  ┌────────────────────────────────────────────────────────┐  │
│  │        Powerful features to boost                      │  │
│  │              productivity                              │  │
│  │   Designed to simplify your workflow, our powerful…    │  │
│  │  ┌───────────────────────┐  ┌───────────────────────┐  │  │
│  │  │ ┌ User Testing ✓ ┐    │  │      ┌──────┐ ┌─────┐ │  │  │
│  │  │┌ Wireframe Home ┐     │  │      │iPhone│ │Work │ │  │  │
│  │  ││ Temlis  [High] │     │  │      │Good  │ │12:09│ │  │  │
│  │  │└────────────────┘     │  │      │morning│└─────┘ │  │  │
│  │  │ [Normal]              │  │      └──────┘          │  │  │
│  │  │ Simple Task Management│  │ Smart Scheduling       │  │  │
│  │  │ Effortlessly create…  │  │ Set due dates…         │  │  │
│  │  └───────────────────────┘  └───────────────────────┘  │  │
│  │  ┌───────────────────────┐  ┌───────────────────────┐  │  │
│  │  │  ┌──────┐ (◉◉◉◉ 🏆)   │  │  ┌─────────────────┐  │  │  │
│  │  │  │iPhone│             │  │  │ 🏆 Goals        │  │  │  │
│  │  │  │My    │             │  │  │ Rona Zepri      │  │  │  │
│  │  │  │tasks │             │  │  │ Task│Time│Proj  │  │  │  │
│  │  │  └──────┘             │  │  │ 10  │10h │ 5    │  │  │  │
│  │  │ Seamless Collaboration│  │  └─────────────────┘  │  │  │
│  │  │ Assign tasks, share…  │  │ Real-Time Notifications│ │  │
│  │  └───────────────────────┘  └───────────────────────┘  │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

#### Relações com outras telas
```
008
 └── mesma origem visual de 004 (cards Task Management / Time Tracking) [INFERIDO]
```

#### Observações
- A legenda usa **nome da feature e descrição no mesmo parágrafo** (negrito/cor escura + cinza), não título separado.
- Mockups são recortes com corte inferior em fade/máscara (iPhone "sangra" para baixo).

---

### Tela 009 — Seção features (cópia)

**Arquivo:** `05_view_comercial-landing-midia 2.JPG` · **ID:** 009

**Relação:** cópia exata da Tela **008** (MD5 `785cdcbe…`, 736×981).
**Diferença observada:** **nenhuma**.

---

### Tela 010 — Pricing 3 planos: Nanodose / Microdose / Customdose

**Arquivo:** `06_view-move-select-card.JPG` · **ID:** 010 · **Resolução:** 735×491 (paisagem, baixa resolução) · **Duplicata:** 011

#### Objetivo da tela
Apresentar três modelos de contratação de um estúdio de design (assinatura, retainer, projeto sob medida), destacando o plano central.

#### Contexto
Seção de pricing dentro de uma moldura branca grande, sobre fundo cinza-claríssimo, com manchas de gradiente pastel (pêssego à esquerda, lilás à direita). Mesma família temática de 002 e da seção de pricing de 018. Resolução baixa: alguns textos pequenos foram lidos por ampliação e marcados `[INCERTO]` quando ambíguos.

#### Estrutura visual
1. Moldura branca (cantos ~24 px) ocupando ~85% da largura.
2. Badge verde-claro no topo (centralizado), título H2, subtítulo.
3. **3 cards em linha**, alinhados pela base visual: esquerdo e direito menores; **central maior, elevado**, com faixa superior em gradiente e borda em gradiente (rosa → laranja no traço inferior; lilás → azul na faixa superior).
4. Cada card: linha de cabeçalho (ícone pequeno + nome do modelo + "…"); nome do plano em 2 pesos (`Nano` negrito + `dose` serifado itálico); tagline; linha com CTA (pílula) à esquerda e preço à direita; lista de features com check.
5. Rodapé centralizado com ícone de folha verde + frase de sustentabilidade.

#### Componentes identificados
| Componente | Posição | Conteúdo | Estado | Interação |
|---|---|---|---|---|
| Badge de disponibilidade | topo centro | `Accepting projects from Q1 2025` `[INCERTO: "Q1"/"01"]` | estático | — |
| Card Nanodose | esquerda | ver texto | default | — |
| Card Microdose | centro | ver texto | **destacado** (maior, faixa `BEST VALUE TO PRICE`, borda gradiente) | — |
| Card Customdose | direita | ver texto | default | — |
| CTA `Get me dose` (Nano) | card esq. | contorno escuro, fundo branco | default | [INCERTO] |
| CTA `Get me dose` (Micro) | card central | fundo sólido azul-violeta, texto branco | primário | [INCERTO] |
| CTA `Book a call` (Custom) | card dir. | contorno escuro | default | agendar chamada `[INFERIDO]` |
| Menu "…" | topo de cada card | três pontos | default | [INCERTO] |
| Nota de sustentabilidade | rodapé | folha verde + texto | estático | — |

#### Conteúdo textual
- Badge: `Accepting projects from Q1 2025` `[INCERTO]`
- H2: `Transparent pricing, with top tier design partner`
- Subtítulo: `Transparent pricing tailored to your needs, ensuring affordability without compromising on quality.`
- **Nanodose** — cabeçalho `Design Subscription` · `Nanodose` · `One request at a time` · CTA `Get me dose` · `$ 4 900/mo` · microtexto `Pause or cancel anytime` · features: `Access to all design services` · `Bi-weekly calls and daily slack communication` · `Available for 3 days each week` · `Easy-to-manage ticketing system` · `Immediate start`
- **Microdose** — faixa `BEST VALUE TO PRICE` · cabeçalho `Retainer` · `Microdose` · `Double your delivery 2x` · CTA `Get me dose` · `$ 8 900/mo` · `Pause or cancel anytime` · features: `All from Nanodose membership` · `Direct comms in Slack + weekly sync` · `No-code development for free` · `Available for 5 days each week` · `Delivery in avg. 48 hours` · `Easy-to-manage ticketing system in Notion` · `Immediate start`
- **Customdose** — cabeçalho `0 → MVP` · `Customdose` · `Fitting your individual project needs` · CTA `Book a call` · microtexto `Starting from` · `$ 10 000/mo` · `50/50 payment` · features: `Custom scope` · `Dedicated team` · `Fixed deadlines` · `Strategic and Consulting Sessions bi-weekly` · `Payment plan based on milestones`
- Rodapé: `Microdose contributes 1% of your subscription to remove CO₂ from the atmosphere through Stripe Climate.`

#### Elementos interativos
- 3 CTAs (`Get me dose` ×2, `Book a call`) — Ação: [INCERTO]
- 3 menus "…" — Ação: [INCERTO]

#### Estado da interface
Default, com o plano central em estado destacado ("recomendado").

#### Wireframe textual
```
┌──────────────────────────────────────────────────────────────────────┐
│                 ( Accepting projects from Q1 2025 )                  │
│           Transparent pricing, with top tier design partner          │
│   Transparent pricing tailored to your needs, ensuring affordability…│
│                              ╔══ BEST VALUE TO PRICE ══╗              │
│  ┌──────────────────────┐    ║ ▫ Retainer          …  ║ ┌───────────┐ │
│  │ ▫ Design Subscr.  …  │    ║                        ║ │▫ 0 → MVP …│ │
│  │ Nano*dose*           │    ║ Micro*dose*            ║ │Custom*dose*│ │
│  │ One request at a time│    ║ Double your delivery 2x║ │Fitting…   │ │
│  │ (Get me dose) $4 900 │    ║ [Get me dose] $8 900   ║ │(Book a    │ │
│  │              /mo     │    ║              /mo       ║ │ call)     │ │
│  │ ✓ Access to all…     │    ║ ✓ All from Nanodose…   ║ │$10 000/mo │ │
│  │ ✓ Bi-weekly calls…   │    ║ ✓ Direct comms Slack…  ║ │ 50/50 pay │ │
│  │ ✓ Available 3 days   │    ║ ✓ No-code development  ║ │✓ Custom…  │ │
│  │ ✓ Easy-to-manage…    │    ║ ✓ Available 5 days     ║ │✓ Dedicated│ │
│  │ ✓ Immediate start    │    ║ ✓ Delivery avg. 48 h   ║ │✓ Fixed…   │ │
│  └──────────────────────┘    ║ ✓ Ticketing in Notion  ║ │✓ Strategic│ │
│                              ║ ✓ Immediate start      ║ │✓ Payment… │ │
│                              ╚════════════════════════╝ └───────────┘ │
│        🍃 Microdose contributes 1% of your subscription to remove CO₂…│
└──────────────────────────────────────────────────────────────────────┘
```

#### Relações com outras telas
```
010
 ├── Get me dose / Book a call -> contato/checkout (não presente) [INFERIDO]
 └── família temática de 002 e da seção de pricing de 018 [INFERIDO]
```

#### Observações
- O card central sobressai por **altura, faixa superior, borda em gradiente e CTA sólido**; os outros usam CTA em contorno.
- Nome do plano usa **dois estilos tipográficos**: sans em negrito (`Nano`, `Micro`, `Custom`) + serif itálica leve (`dose`), cor azul-acinzentada.
- Preço: símbolo `$` pequeno, valor grande, `/mo` pequeno e cinza.

---

### Tela 011 — Pricing 3 planos (cópia)

**Arquivo:** `06_view-move-select-card 2.JPG` · **ID:** 011

**Relação:** cópia exata da Tela **010** (MD5 `3d0aca8f…`, 735×491).
**Diferença observada:** **nenhuma**.

---

### Tela 012 — Seção "We've orchestrated Intelligence."

**Arquivo:** `07_view-store-select.JPG` · **ID:** 012 · **Resolução:** 454×381 (baixa resolução) · **Duplicata:** 013

#### Objetivo da tela
Apresentar a proposta de valor de uma plataforma de agentes de IA corporativos, com 4 pilares numerados; um deles (o 02) está expandido.

#### Contexto
Seção de hero/intro de landing page de IA (marca `Metafore`, lida no parágrafo; `[INCERTO]` pela baixa resolução). O nome do arquivo ("store-select") sugere seleção de card, e a imagem de fato mostra **card selecionado/expandido**.

#### Estrutura visual
- Fundo `#F8F8F8` com **grade fina** de linhas ao fundo (visível na metade superior-direita).
- **Coluna esquerda superior:** chip `MISSION` com ícone; H1 em 2 linhas (`We've orchestrated` preto / `Intelligence.` verde-petróleo).
- **Coluna direita superior:** parágrafo pequeno cinza + botão escuro em pílula.
- **Linha de 4 cards** (mesma linha de base inferior visual, alturas diferentes):
  - 01: card branco estreito, numeral grande cinza-claro `01.`, ícone + título no rodapé.
  - 02: **card expandido** (~2× largura e mais alto), imagem 3D de linhas onduladas verde-água/cinza no topo, ícone, título grande, parágrafo no rodapé.
  - 03 e 04: cards estreitos como o 01.
- Ícone circular (refresh/sparkle) no canto inferior direito.

#### Componentes identificados
| Componente | Posição | Conteúdo | Estado | Interação |
|---|---|---|---|---|
| Chip `MISSION` | sup. esq. | ícone + texto mono caixa-alta | estático | — |
| H1 bicolor | sup. esq. | `We've orchestrated` + `Intelligence.` (cor de destaque verde-petróleo) | — | — |
| Parágrafo | sup. dir. | texto | — | — |
| Botão `Explore More` | sup. dir. | fundo quase preto, texto branco pequeno | default | [INCERTO] |
| Card 01 | linha, col. 1 | `01.` + ícone raio + `Amplify Intelligence` | **colapsado** | expandir ao clicar/hover `[INFERIDO]` |
| Card 02 | linha, col. 2 | imagem + ícone globo + `Command Global Operations` + parágrafo | **expandido/ativo** | — |
| Card 03 | linha, col. 3 | `03.` + ícone link + `Eliminate Silos` | colapsado | idem |
| Card 04 | linha, col. 4 | `04.` + ícone gráfico + `Scale with Clarity` | colapsado | idem |
| Ícone flutuante | canto inf. dir. | círculo com seta/faísca | [INCERTO] | [INCERTO] |

#### Conteúdo textual
`MISSION` · `We've orchestrated` · `Intelligence.` · `Metafore brings clarity, not complexity — uniting every ^agent into one adaptive system that learns, acts, and evolves across your enterprise.` (o "^" antes de `agent` é um glifo/ícone inline `[INCERTO]`) · `Explore More` · `01.` `Amplify Intelligence` · `Command Global Operations` · `Coordinate your entire organization through orchestrated ^agents that ensure precision, compliance, and efficiency everywhere you operate.` · `03.` `Eliminate Silos` · `04.` `Scale with Clarity`
> O numeral `02.` não está visível no card expandido (substituído pela imagem) `[INFERIDO]`.

#### Elementos interativos
- `Explore More` — Ação: [INCERTO]
- Cards 01–04 — comportamento de accordion horizontal `[INFERIDO]` (um expandido, três colapsados)
- Ícone do canto inferior direito — Ação: [INCERTO]

#### Estado da interface
Item 02 selecionado/expandido; itens 01, 03, 04 colapsados.

#### Wireframe textual
```
┌──────────────────────────────────────────────────────────────────────┐
│ [◈ MISSION]                                                          │
│ We've orchestrated                    Metafore brings clarity, not…  │
│ Intelligence.  (verde-petróleo)       …evolves across your enterprise│
│                                       ( Explore More )               │
│                    ┌─────────────────────┐                           │
│                    │ ~~~ imagem 3D ondas │                           │
│ ┌─────────┐        │ ~~~ verde-água ~~~~ │  ┌────────┐ ┌────────┐     │
│ │ 01.     │        │                     │  │ 03.    │ │ 04.    │     │
│ │         │        │ ◍                   │  │        │ │        │     │
│ │         │        │ Command Global      │  │        │ │        │     │
│ │ ⚡      │        │ Operations          │  │ 🔗     │ │ ◔      │     │
│ │ Amplify │        │                     │  │Eliminate│ │Scale   │     │
│ │ Intellig│        │ Coordinate your     │  │ Silos  │ │with    │     │
│ └─────────┘        │ entire organization…│  └────────┘ │Clarity │     │
│                    └─────────────────────┘             └────────┘  ⟳  │
└──────────────────────────────────────────────────────────────────────┘
```

#### Relações com outras telas
```
012
 └── Explore More -> página de detalhes (não presente) [INFERIDO]
```

#### Observações
- Cards colapsados têm numeral gigante em cinza-muito-claro e conteúdo alinhado à base; o expandido usa hierarquia invertida (imagem topo, título médio, parágrafo base).
- Tipografia: sans grotesca de display (H1) + mono para chip `MISSION`.

---

### Tela 013 — Seção Intelligence (cópia)

**Arquivo:** `07_view-store-select 2.JPG` · **ID:** 013

**Relação:** cópia exata da Tela **012** (MD5 `c6222f25…`, 454×381).
**Diferença observada:** **nenhuma**.

---

### Tela 014 — Wireframe de landing page (desktop + mobile)

**Arquivo:** `08_viewlandingpage.JPG` · **ID:** 014 · **Resolução:** 236×419 (**muito baixa**; texto pequeno ilegível) · **Duplicata:** 015

#### Objetivo da tela
Servir de **wireframe de baixa fidelidade** de landing page de imobiliária/decoração, com versão desktop e mobile lado a lado.

#### Contexto
Única imagem do conjunto em escala de cinza pura (wireframe). Estrutura útil como esqueleto de landing page; o texto de corpo é `[TEXTO ILEGÍVEL]` (barras).

#### Estrutura visual
Duas colunas verticais:
- **Coluna esquerda (~2/3, desktop):** sequência de seções empilhadas:
  1. **Hero** (bloco cinza-escuro): H1 `Find Your Dream Home With Ease.`, texto de apoio, botão preto + link secundário; à direita placeholder de imagem.
  2. **Faixa de 3 destaques** (círculo/ícone + título + linha de texto ×3).
  3. **Listagem**: barra de filtros (pílulas/tabs) + controles de carrossel (setas, ponto preto); **3 cards** de imóvel (placeholder de imagem, título, descrição, preço à esquerda, botão preto à direita); indicador de paginação.
  4. **`User guide for first timer`**: título grande à esquerda; à direita lista vertical `Step 1 … Step 4` com linha vertical escura.
  5. **`Satisfied Clients Speaks`**: colagem de 2 placeholders de imagem + card de depoimento (avatar, nome, linhas de texto) + botão preto em pílula com ponto.
  6. **Estatísticas + destaque**: coluna esquerda `10+ Million`, `8x More`, `1+ Million` (cada um com 2 linhas); imagem alta central; à direita título + parágrafo `[TEXTO ILEGÍVEL]` (lê-se algo como "…The Transformation Of Real-estate" `[INCERTO]`).
  7. **`Blog Section`**: título centralizado + setas; carrossel de 4 cards (imagem, texto, preço, botão preto).
  8. **`Services`**: 3 cards numerados: `01 Furniture Design` (card **preto**, texto branco), `02 Interior Details`, `03 Home Revamping` (brancos).
  9. **Rodapé** (barra cinza-escuro, cortada).
- **Coluna direita (~1/4, mobile):** as mesmas seções empilhadas em largura de smartphone (hero, círculos, cards, `User guide for first timer`, `Satisfied Clients Speaks`, estatísticas). `[INFERIDO]` por silhueta; conteúdo interno ilegível.

#### Componentes identificados
Placeholder de imagem (ícone montanha/sol em quadrado cinza), botão preto pequeno, card de imóvel, barra de filtros, carrossel com setas/ponto, accordion/lista de passos, card de depoimento, bloco de estatística, card de serviço (variação preta/branca), rodapé.

#### Conteúdo textual (legível)
`Find Your Dream Home With Ease.` · `User guide for first timer` · `Step 1`, `Step 2`, `Step 3`, `Step 4` · `Satisfied Clients Speaks` · `10+ Million` · `8x More` · `1+ Million` · `Blog Section` · `Services` · `01 Furniture Design` · `02 Interior Details` · `03 Home Revamping`. Todo o restante: [TEXTO ILEGÍVEL].

#### Elementos interativos
- Botões pretos (hero, cards, depoimento) — Ação: [INCERTO]
- Filtros/tabs e setas de carrossel (listagem e blog) — Ação: navegar/filtrar `[INFERIDO]`
- Card de serviço `01` em estado preto: possível estado ativo/hover `[INFERIDO]`

#### Estado da interface
Wireframe estático (sem estados reais). O card `01 Furniture Design` está invertido (preto), sugerindo seleção.

#### Wireframe textual
```
┌──────────────────────────────────────────────────┐ ┌──────────┐
│ ▓▓▓ Hero (cinza-escuro) ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │ │ ▓ hero ▓ │
│ Find Your Dream                  ┌──────────────┐│ │ ▓ img  ▓ │
│ Home With Ease.                  │   [🖼 img]   ││ ├──────────┤
│ texto…  [■ botão] link           └──────────────┘│ │ ● txt    │
├──────────────────────────────────────────────────┤ │ ● txt    │
│ ◯ título/linha    ◯ título/linha   ◯ título/linha│ │ ● txt    │
├──────────────────────────────────────────────────┤ ├──────────┤
│ [tab][tab][tab]                          ‹  ●    │ │ [🖼]     │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐           │ │ título   │
│ │  [🖼]    │ │  [🖼]    │ │  [🖼]    │           │ │ preço [■]│
│ │ título   │ │ título   │ │ título   │           │ ├──────────┤
│ │ preço [■]│ │ preço [■]│ │ preço [■]│           │ │ User     │
│ └──────────┘ └──────────┘ └──────────┘           │ │ guide…   │
│                    ▬  (paginação)                │ │ Step 1…4 │
├──────────────────────────────────────────────────┤ ├──────────┤
│ User guide for              │ ▏Step 1  texto     │ │ Satisfied│
│ first timer                 │ ▏Step 2  texto     │ │ Clients  │
│                             │ ▏Step 3  texto     │ │ [🖼]card │
│                             │ ▏Step 4  texto     │ ├──────────┤
├──────────────────────────────────────────────────┤ │ 10+ Mill.│
│              Satisfied Clients Speaks            │ │ 8x More  │
│ ┌────┐┌─────┐  ┌────────────────────────────┐   │ │ 1+ Mill. │
│ │[🖼]││ [🖼]│  │ ◯ nome  · texto…           │   │ └──────────┘
│ └────┘└─────┘  │ [■■■■■■■■■■■■■■■■■■■■ ●]   │   │
├──────────────────────────────────────────────────┤
│ 10+ Million  │        │ título…                  │
│ 8x More      │ [🖼]   │ parágrafo…               │
│ 1+ Million   │        │                          │
├──────────────────────────────────────────────────┤
│               Blog Section                  ‹ ●  │
│ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐          │
│ │ [🖼]  │ │ [🖼]  │ │ [🖼]  │ │ [🖼]  │  →       │
│ │ preço │ │ preço │ │ preço │ │ preço │          │
│ └───────┘ └───────┘ └───────┘ └───────┘          │
├──────────────────────────────────────────────────┤
│                    Services                      │
│ ┌────────┐ ┌────────┐ ┌────────┐                 │
│ │■■ 01   │ │   02   │ │   03   │                 │
│ │Furniture│ │Interior│ │Home    │                 │
│ │Design  │ │Details │ │Revamp. │                 │
│ └────────┘ └────────┘ └────────┘                 │
├──────────────────────────────────────────────────┤
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ rodapé (cortado) ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
└──────────────────────────────────────────────────┘
```

#### Relações com outras telas
```
014
 └── serve como esqueleto estrutural para landing pages 004 e 018 [INFERIDO]
```

#### Observações
- Resolução extremamente baixa: a ordem das seções foi lida com segurança, mas tamanhos relativos e textos pequenos são aproximados.
- Padrão de repetição: cards de conteúdo com **preço à esquerda e botão preto à direita** (listagem e blog).

---

### Tela 015 — Wireframe de landing page (cópia)

**Arquivo:** `08_viewlandingpage 2.JPG` · **ID:** 015

**Relação:** cópia exata da Tela **014** (MD5 `fef933a6…`, 236×419).
**Diferença observada:** **nenhuma**.

---

### Tela 016 — Card de tarefa Kanban: "CRM Layout Draft"

**Arquivo:** `10_viewcard-.JPG` · **ID:** 016 · **Resolução:** 1199×1176 (quase quadrada)

#### Objetivo da tela
Apresentar o **componente de card de tarefa** de um board (etiqueta de coluna/estágio, título, resumo, responsáveis, status, contadores e data).

#### Contexto
Componente isolado, exibido em "modo canvas de design" (ferramenta estilo Figma). Relaciona-se tematicamente com o ecossistema de tarefas de 004/008, mas com visual próprio. O nome do arquivo (`10_viewcard-`) não corresponde a `10_viewcard-group` (017), que é uma cópia de 001.

#### Estrutura visual
- **Canvas** cinza `#EBEBEB` com pontilhado e **duas linhas-guia** cruzando (horizontais e verticais) formando retângulo de seleção; **4 alças** octogonais nas interseções.
- **Placa/moldura** cinza-clara com cantos ~40 px e 4 "parafusos" nos cantos (efeito skeuomórfico), contendo o card.
- **Card** (cantos ~28 px, sombra): 
  - **Faixa superior azul** (`#4AB3F7` amostrado) com texto `ON BOARDING` branco, caixa-alta, centralizado.
  - **Corpo** com **caixa interna de borda tracejada**: título; descrição truncada (2 linhas + reticências); linha com **avatares sobrepostos** (4) à esquerda e **chip de status** `In Progress` à direita.
  - **Rodapé:** 3 contadores com ícone (comentários `8`, links `4`, anexos/pastas `12`) à esquerda; data `September, 17` à direita em cinza.

#### Componentes identificados
| Componente | Posição | Conteúdo | Estado | Interação |
|---|---|---|---|---|
| Faixa de estágio | topo do card | `ON BOARDING` | azul (cor por estágio) `[INFERIDO]` | — |
| Título | corpo | `CRM Layout Draft` | — | abrir tarefa `[INFERIDO]` |
| Descrição | corpo | `Designing the basic structure of the CRM dashboard. Focus on organizing customer data,…` | truncada | — |
| Avatares | corpo, esq. | 4 fotos circulares sobrepostas | — | ver responsáveis `[INFERIDO]` |
| Chip de status | corpo, dir. | `In Progress` (cinza sobre cinza-claro) | status atual | alterar status `[INFERIDO]` |
| Contador comentários | rodapé | ícone balão + `8` | — | [INCERTO] |
| Contador links | rodapé | ícone corrente + `4` | — | [INCERTO] |
| Contador anexos | rodapé | ícone pasta + `12` | — | [INCERTO] |
| Data | rodapé, dir. | `September, 17` | — | — |
| Alças de seleção / guias | canvas | 4 nós + linhas | modo edição de design | não fazem parte do produto |

#### Conteúdo textual
`ON BOARDING` · `CRM Layout Draft` · `Designing the basic structure of the CRM dashboard. Focus on organizing customer data,…` · `In Progress` · `8` · `4` · `12` · `September, 17`

#### Elementos interativos
Todo o card é provavelmente clicável `[INFERIDO]`; ícones do rodapé e avatares possivelmente abrem painéis. Ação: [INCERTO]

#### Estado da interface
Card default (não hover, não arrastado). Ambiente de apresentação mostra o card "selecionado" no canvas de design (alças) — não é estado do produto.

#### Wireframe textual
```
┌───────────────────────────────────────────────────────────────┐
│ (canvas cinza pontilhado)                                     │
│   ◈─────────────────────────────────────────────────◈        │
│   │     ┌───────────────────────────────────────┐   │        │
│   │     │ ∙ ┌───────────────────────────────┐ ∙ │   │        │
│   │     │   │▓▓▓▓▓▓▓  ON BOARDING  ▓▓▓▓▓▓▓▓ │   │   │        │
│   │     │   ├───────────────────────────────┤   │   │        │
│   │     │   │ ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐ │   │   │        │
│   │     │   │ ╎ CRM Layout Draft           ╎ │   │   │        │
│   │     │   │ ╎ Designing the basic struc- ╎ │   │   │        │
│   │     │   │ ╎ ture of the CRM dashboard… ╎ │   │   │        │
│   │     │   │ ╎ (◉)(◉)(◉)(◉)   [In Progress]╎│   │   │        │
│   │     │   │ └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘ │   │   │        │
│   │     │   │ 💬 8   🔗 4   🗂 12  September,17│  │   │        │
│   │     │ ∙ └───────────────────────────────┘ ∙ │   │        │
│   │     └───────────────────────────────────────┘   │        │
│   ◈─────────────────────────────────────────────────◈        │
└───────────────────────────────────────────────────────────────┘
```

#### Relações com outras telas
```
016
 └── conceito de tarefa/card -> alinhado a 004/008 (gestão de tarefas) [INFERIDO]
```

#### Observações
- A faixa azul lê como **etiqueta de estágio/coluna** (ex.: `ON BOARDING`); outras cores para outros estágios seriam esperadas `[INFERIDO]`, mas não são mostradas.
- A borda **tracejada** do bloco interno é elemento visual deliberado (não indica "arrastar" com certeza) `[INCERTO]`.
- Moldura com parafusos e sombras dá aspecto de "placa física" — é decoração da apresentação.

---

### Tela 017 — ChatGPT iPad "Add files" (cópia com nome divergente)

**Arquivo:** `10_viewcard-group.JPG.PNG` · **ID:** 017

**Relação:** cópia exata da Tela **001** (MD5 `d73524d9…`, 1640×2360).
**Diferença observada:** **nenhuma no conteúdo**; muda apenas o **nome** (`10_viewcard-group.JPG.PNG` vs `01_View-group.PNG`; dupla extensão `.JPG.PNG` ocorre no nome, mas o formato real é PNG). Por seu nome, `[INFERIDO]` foi salva como "card group" mas é um screenshot de chat, não um agrupamento de cards.

---

### Tela 018 — Landing page fintech "Payno" (página completa em 2 colunas)

**Arquivo:** `11_view comcercial full pront.jpeg` · **ID:** 018 · **Resolução:** 1199×1499 (retrato)

#### Objetivo da tela
Mostrar uma **landing page comercial completa** (hero → benefícios → pricing → prova social → CTA final) de um app fintech, em uma única imagem dividida em **2 colunas** de leitura (esquerda = início da página; direita = continuação).

#### Contexto
Page-length preview (estilo vitrine Dribbble/Behance). Fundo com **céu azul e nuvens**, cards de vidro fosco (glassmorphism), mockups de iPhone (inclusive em mão segurando). Leitura: coluna esquerda de cima para baixo, depois coluna direita de cima para baixo `[INFERIDO]` — a coluna direita começa com formulário de pagamento e termina com CTA final, o que indica continuação.

#### Estrutura visual — Coluna esquerda
1. **Hero (moldura arredondada azul-céu):**
   - Navbar: logo `payno` (esq.), pílula translúcida com links `Home` (ativo, com fundo), `Watch`, `About Us`, `FAQ`, `Blog`; botão branco `Download App` (dir.).
   - H1 à esquerda `Take Control of Your Stock`; parágrafo e botão `Get Start` (contorno) à direita.
   - Centro: mão segurando iPhone (tela do app: saudação `Welcome back Jerome Bell`, saldo `$56,750.00`, `Quick Actions` [`Send`, `Add Funds`, `Pay Bills`, `Transfer`], `Recent transactions` [`Paypal` `+$80.89`, `Google one` `-$0.99`, …], tab bar inferior com botão `+` central).
   - Cards flutuantes: sparkline com `1,235` e `456`; cartão `Projected limit` `$15k` `Per day` com avatares; card de vidro com **gráfico de rosca** e legenda.
2. **Ícone decorativo:** ondas concêntricas azuis desfocadas (centro).
3. **Manchete central em 3–4 linhas:** `From Budgeting to Investing—We've Got You Covered. Getting Ahead with` **`Money`** (azul) `Has Never Been This Simple`.
4. **Bloco 2 colunas:** à esquerda card com iPhone `Send Money` (`Recent Recipients` com avatares e `Add New`, campos de valor `$1,250.00` com seletor de moeda `USD`, `Select Payment Method`); à direita `Built for Simplicity. Designed for Growth.` + parágrafo + **grade 2×2 de features**: `Real-Time Analytics`, `Secure Cloud Sync`, `Smart Budget Alerts`, `Fast Bank Integration` (cada uma com ícone, título e descrição de 2 linhas).
5. **Título (cortado):** `Smart Finance Management Made Simple Today`.

#### Estrutura visual — Coluna direita
1. **Dois cards de vidro lado a lado:**
   - Formulário de pagamento: `We're paying for` + select com avatar `Jacob Jones`; `Pay with` + opção segmentada `Card` / `Bank Account` (Bank Account marcado); campo de cartão `1234 1234 1234 1234`; `Expiration` `MM/YY`, `CVC 123` com ícone; botão azul-escuro `Get Start`. Legenda abaixo: `Transaction Tracking System` + texto `Keep track of all subscriptions, upcoming bills, and payment history without missing deadlines.`
   - `Upcoming Bills` com link `Detail`: linhas `Paypal` `Today, 5:30 PM` `+$80.89`, `Google one`, `Apple`, `Amazon`, `Dribbble Pro` (cada uma com ícone de marca, horário e valor colorido). Legenda idêntica `Transaction Tracking System`.
2. **`Finance Made Simple For Everyone`** (esquerda) — lista vertical com divisores: `Real-time balance updates`, `Automated savings tools` (item **expandido** com descrição `Monitor transactions instantly with accurate insights for smarter business growth.` e barra de progresso/underline azul), `Secure digital payments`, `Multi-device synchronization`, `Instant monthly reports`; (direita) card azul com iPhone `Earning` (`Total Earn`, `$56.75`, dois cards `$19,270.56`).
3. **`Flexible Pricing Plans Built for Everyone Globally`** — toggle `Monthly / Yearly` (Yearly ativo? `[INCERTO]`) + 3 cards de plano:
   - `Starter Plan` — `Free` — botão `Get Started` — 5 features (`[TEXTO ILEGÍVEL]` parcial)
   - `Pro Plan` — `$12 /month` — **destacado** (maior, cabeçalho azul-escuro `Most Popular`, botão sólido azul-escuro `Get Started`, ícones de check escuros) — 5 features
   - `Business` — `$29 /month` — botão `Get Started` — 5 features
4. **`Trusted by Smart Investors and Everyday Savers`** — carrossel de depoimentos (4 visíveis, o último cortado): aspas grandes, texto pequeno, avatar + nome: `Emery George`, `Cooper Curtis`, `Sarah Mitchell`, [TEXTO ILEGÍVEL].
5. **CTA final:** `Take Full Control of Your Financial Future` + subtítulo + botões `Download App` / `Get Started` (par segmentado) + iPhone em mão com gráfico `BTC` (linha verde, tooltip).

#### Componentes identificados
| Componente | Onde | Descrição |
|---|---|---|
| Navbar em pílula | hero | logo + links + CTA `Download App` |
| Hero com mockup em mão | hero | iPhone fotorrealista + cards flutuantes de vidro |
| Manchete central | após hero | tipografia clara, palavra `Money` em azul |
| Card com phone `Send Money` | bloco 2 | mockup de tela de transferência |
| Grade 2×2 de features | bloco 2 | ícone + título + descrição |
| Formulário de pagamento | col. dir. topo | select, segmented, inputs, CTA |
| Lista `Upcoming Bills` | col. dir. topo | linhas com ícone, hora, valor |
| Lista de benefícios (accordion) | col. dir. | 1 item expandido |
| Toggle `Monthly / Yearly` | pricing | alterna período |
| 3 cards de plano | pricing | `Starter`/`Pro`(destaque)/`Business` |
| Carrossel de depoimentos | prova social | cards de vidro, avatar + nome |
| CTA final com mockup | rodapé | 2 botões + phone |

#### Conteúdo textual
Transcrito nas seções acima. Textos pequenos dentro dos mockups e das listas de features de pricing são em grande parte `[TEXTO ILEGÍVEL]`; valores `Free`, `$12`, `$29`, `$56,750.00`, `$1,250.00`, `$56.75`, `$19,270.56` foram lidos com razoável confiança.

#### Elementos interativos
- Links da navbar (`Home`, `Watch`, `About Us`, `FAQ`, `Blog`) — Ação: navegar por âncora/página `[INFERIDO]`
- `Download App` (×2), `Get Start`, `Get Started` (×N) — Ação: [INCERTO]
- Select `Jacob Jones`, opção `Card` / `Bank Account`, campos de cartão — formulário funcional `[INFERIDO]`
- Toggle `Monthly / Yearly` — alterna preços `[INFERIDO]`
- Lista de benefícios — expandir/colapsar `[INFERIDO]`
- Carrossel de depoimentos — rolagem horizontal `[INFERIDO]` (card cortado à direita)

#### Estado da interface
Default de página completa. Estados destacados: `Home` ativo na navbar; `Bank Account` selecionado; `Automated savings tools` expandido; `Pro Plan` destacado; um toggle mensal/anual em uma posição.

#### Wireframe textual
```
COLUNA ESQUERDA (início da página)               COLUNA DIREITA (continuação)
┌──────────────────────────────────────────┐    ┌──────────────────────────────────┐
│ payno   (Home Watch About FAQ Blog) [Dl] │    │ ┌────────────┐ ┌────────────┐    │
│                                          │    │ │We're paying│ │Upcoming    │    │
│ Take Control        Our all-in-one…      │    │ │for [Jacob▾]│ │Bills Detail│    │
│ of Your Stock       [Get Start]          │    │ │Pay with    │ │ Paypal +80 │    │
│   ┌─────┐  ┌sparkline┐                   │    │ │(Card)(Bank)│ │ Google one │    │
│   │📱 mão│  │1,235 456│ ┌donut┐          │    │ │1234 1234…  │ │ Apple      │    │
│   │saldo │  └─────────┘ └─────┘          │    │ │MM/YY  CVC  │ │ Amazon     │    │
│   │$56,750│  [limit $15k ◉◉◉]            │    │ │[Get Start] │ │ Dribbble   │    │
│   └─────┘                                │    │ └────────────┘ └────────────┘    │
├──────────────────────────────────────────┤    │ Transaction Tracking System ×2   │
│                ◔◔◔ (ondas)               │    ├──────────────────────────────────┤
│   From Budgeting to Investing—We've Got  │    │ Finance Made      ┌────────────┐ │
│   You Covered. Getting Ahead with        │    │ Simple For        │ 📱 Earning │ │
│   Money Has Never Been This Simple       │    │ Everyone          │ $56.75     │ │
├──────────────────────────────────────────┤    │ Real-time balance │ $19,270 ...│ │
│ ┌─────────────┐ Built for Simplicity.    │    │ Automated savings │ └────────────┘ │
│ │📱 Send Money│ Designed for Growth.     │    │  └ descrição ▬▬▬                 │
│ │ Recipients  │ ┌──────────┐┌──────────┐ │    │ Secure digital payments          │
│ │ $1,250 USD  │ │Real-Time ││Secure    │ │    │ Multi-device synchronization     │
│ │ Select Pay… │ │Analytics ││Cloud Sync│ │    │ Instant monthly reports          │
│ └─────────────┘ ├──────────┤├──────────┤ │    ├──────────────────────────────────┤
│                 │Smart     ││Fast Bank │ │    │ Flexible Pricing Plans Built for │
│                 │Budget…   ││Integrat. │ │    │ Everyone Globally  (Monthly|Yearly)
├──────────────────────────────────────────┤    │ ┌───────┐╔═Most Popular╗┌───────┐│
│ Smart Finance Management                 │    │ │Starter│║ Pro Plan    ║│Business││
│ Made Simple Today  (cortado)             │    │ │ Free  │║ $12/month   ║│$29/mo  ││
└──────────────────────────────────────────┘    │ │ ✓✓✓✓✓ │║ [Get Started]║│ ✓✓✓✓✓ ││
                                                │ └───────┘╚═════════════╝└───────┘│
                                                ├──────────────────────────────────┤
                                                │ Trusted by Smart Investors and   │
                                                │ Everyday Savers                  │
                                                │ ❝ Emery ❝ Cooper ❝ Sarah ❝ …   │
                                                ├──────────────────────────────────┤
                                                │ Take Full Control of Your        │
                                                │ Financial Future                 │
                                                │ (Download App)(Get Started)      │
                                                │       📱 BTC chart em mão        │
                                                └──────────────────────────────────┘
```

#### Relações com outras telas
```
018
 ├── seção de pricing         -> mesma família de 002 e 010 [INFERIDO]
 ├── mockups de app           -> mesma técnica de 004/008 [INFERIDO]
 └── estrutura hero→features→pricing→depoimentos→CTA -> mesma lógica do wireframe 014 [INFERIDO]
```

#### Observações
- Estética: **glassmorphism** sobre céu; bordas 1 px branco translúcido; sombras muito suaves.
- Cores dominantes: azul-céu, branco, azul-marinho acinzentado nos textos e CTAs.
- Pricing usa o mesmo padrão de **plano central em destaque** de 010 (maior + cabeçalho colorido).
- A divisão em duas colunas é do **arquivo de apresentação**, não de um layout de duas colunas real do site.

---

## 6. Componentes Compartilhados

> "Presente em" lista o ID canônico e, entre parênteses, as duplicatas idênticas.

### Component: Card de plano (Pricing Card)

**Presente em:** 002 (003), 010 (011), 018 (seção pricing)

**Estrutura**
- Container branco com cantos grandes (≈ 24–32 px), sombra suave, borda opcional (fina, gradiente em 002 e 010).
- Cabeçalho: nome do plano; opcional badge (`POPULAR` em 002; faixa `BEST VALUE TO PRICE` em 010; `Most Popular` em 018).
- Preço: valor grande + unidade pequena (`/ month`, `/mo`, `/month`).
- Tagline/subtítulo.
- Divisor (002) ou linha de CTA (010).
- Lista de features com ícone de check.
- CTA: aba inferior em gradiente (002), pílula no cabeçalho (010), botão largo no fim (018).

**Conteúdo:** nome, preço, período, lista de 4–7 benefícios, CTA.

**Estados observados:** default; **destacado** (002 esquerdo via badge; 010 central maior com borda gradiente; 018 `Pro Plan` maior com cabeçalho escuro).

**Variações:**
| ID | Nº planos | Destaque | CTA |
|---|---|---|---|
| 002 | 2 | badge escuro `POPULAR` | aba de gradiente colada ao card |
| 010 | 3 | card central maior + faixa | contorno (laterais) / sólido (central) |
| 018 | 3 | card central maior, cabeçalho azul-escuro | botão dentro do card |

**Comportamento inferido:** CTA leva ao checkout/contato; em 018 o toggle `Monthly / Yearly` altera preço `[INFERIDO]`.

---

### Component: Badge / Pílula de rótulo

**Presente em:** 002 (`POPULAR`), 004 (`COMING SOON`, `TEMPLATES`), 010 (badge de disponibilidade, `BEST VALUE TO PRICE`), 012 (`MISSION`), 016 (`ON BOARDING` como faixa), 016 (chip `In Progress`), 008 (tag `High Priority`)

**Estrutura:** texto curto (caixa-alta em vários) em contêiner arredondado (pílula/retângulo de canto grande).
**Estados observados:** estático; cor semântica (escuro, azul, verde-claro, vermelho em tag).
**Comportamento inferido:** apenas informativo, sem clique.

---

### Component: CTA em pílula

**Presente em:** 002, 004, 010, 012, 014 (botões pretos), 018

**Variações:** gradiente (002), branco (004, 018 navbar), preto/escuro (012, 014, 018), contorno (010), sólido azul-violeta (010), integrado em campo de input (004).
**Estados:** somente default visível; hover/active/disabled [INCERTO].

---

### Component: Lista de features com check

**Presente em:** 002, 010, 018

**Estrutura:** ícone de check à esquerda + texto; em 002 título + descrição em 2 linhas; em 010 e 018 apenas 1 linha.
**Variações:** check tricolor (002), check cinza/verde suave (010), check escuro (018 Pro).

---

### Component: Mockup de iPhone

**Presente em:** 004 (hero + card Time Tracking), 008 (cards 2 e 3), 018 (hero, `Send Money`, `Earning`, CTA final)

**Estrutura:** moldura preta com Dynamic Island; status bar `9:41`; tela do app. Frequentemente cortado na base com fade; cartões flutuantes (chip `Work this week`, avatares, gráficos) sobrepõem a borda.
**Comportamento:** ilustrativo, sem interação.

---

### Component: Card de feature com ilustração

**Presente em:** 004 (`Task Management`, `Time Tracking`), 008 (grade 2×2), 012 (cards numerados), 018 (grade 2×2 com ícone)

**Estrutura:** área visual (mockup/ícone/imagem) + título + descrição curta.
**Variações:** ilustração grande (004/008), ícone pequeno (018), numeral grande + ícone (012), expandido/colapsado (012).

---

### Component: Card de tarefa

**Presente em:** 016 (componente completo); versões miniaturizadas dentro dos mockups de 004 e 008 (`Final Design Review`, `Wireframe Homepage`)

**Estrutura (016):** faixa de estágio → título → descrição → avatares + status → contadores + data.
**Estados observados:** default; em 008 há também **checked/concluído esmaecido** (`User Testing`) e **destacado por elevação** (`Wireframe Homepage`).
**Comportamento inferido:** arrastável entre colunas de board `[INFERIDO]`.

---

### Component: Avatar stack

**Presente em:** 008 (card 3), 016, 018 (limite de gasto, destinatários)

**Estrutura:** 3–4 avatares circulares sobrepostos, borda branca; opcional ícone/troféu ao final (008).

---

### Component: Modal / Bottom sheet de seleção de arquivos

**Presente em:** 001 (017)

**Estrutura:** header (fechar / título / menu), ação primária (`Upload files`), seção `Recent`, grade 3 colunas, busca flutuante.
**Estados observados:** aberto; um item em loading (skeleton); nenhum selecionado.

---

### Component: Navbar de landing

**Presente em:** 004 (logo + botão), 018 (logo + pílula de links + CTA)

**Variações:** simples (004) vs. completa com nav em pílula translúcida (018).
**Estado ativo:** `Home` em 018 com fundo destacado.

---

### Component: Formulário embutido

**Presente em:** 004 (e-mail + `JOIN WAITLIST` em uma pílula), 018 (pagamento e transferência)
**Campos observados (018):** select com avatar; segmented control `Card`/`Bank Account`; input de número de cartão; `MM/YY`; `CVC`; input de valor com seletor de moeda.
**Validação/erro:** não mostrados.

---

### Component: Widget de métricas

**Presente em:** 006 (007)

**Estrutura:** título de seção + cartão grande com coluna de ícone/resumo e coluna de tiles (rótulo cinza + valor em negrito).

---

### Component: Placeholder de imagem (wireframe)

**Presente em:** 014 (015)
**Estrutura:** quadrado cinza com ícone de montanha/sol; usado em hero, cards, colagem, estatísticas e blog.

---

## 7. Mapa de Navegação

As imagens **não formam um app único**. O mapa abaixo agrupa por **função de referência**, não por rotas reais. Setas (→) só aparecem onde a própria imagem mostra ou implica navegação.

```
Coleção de referências (Archive_2.zip)
├── Contexto de uso / ferramenta
│   └── 001 ChatGPT iPad — modal "Add files"  (017 = cópia)
│        └── [modal] Upload files | Recent | Search library
│
├── Pricing
│   ├── 002 Personal vs Business (2 planos)  (003 = cópia)
│   ├── 010 Nano/Micro/Customdose (3 planos)  (011 = cópia)
│   └── 018 (seção "Flexible Pricing Plans", 3 planos)
│
├── Landing pages / seções
│   ├── 004 Nearo "Coming Soon" (hero + features + countdown)  (005 = cópia)
│   ├── 008 "Powerful features…" (grade 2×2)  (009 = cópia)
│   ├── 012 "We've orchestrated Intelligence." (accordion de 4 cards)  (013 = cópia)
│   └── 018 Payno (landing completa, 2 colunas)
│        ├── Hero → Manchete → Features → [col. 2] Pagamento/Contas → Benefícios
│        └── → Pricing → Depoimentos → CTA final
│
├── Wireframe estrutural
│   └── 014 Landing imobiliária/decoração (desktop + mobile)  (015 = cópia)
│        └── Hero → Destaques → Listagem → User guide → Depoimentos → Estatísticas → Blog → Services → Footer
│
├── Componentes isolados
│   ├── 016 Card de tarefa Kanban "CRM Layout Draft"
│   └── 006 Widget Privacy Report (Safari)  (007 = cópia)
```

Ordem interna de leitura demonstrada apenas dentro de páginas longas (004, 014, 018).

---

## 8. Inventário Final

### 8.1 Números
| Métrica | Valor |
|---|---|
| Arquivos de imagem no ZIP | **18** (+ metadados `__MACOSX`, ignorados) |
| Imagens **distintas** (por MD5) | **10** |
| Duplicatas exatas | **8 arquivos** (pares 002/003, 004/005, 006/007, 008/009, 010/011, 012/013, 014/015, 001/017) |
| Número de arquivo ausente na sequência | `09` |
| Telas "de produto real" | 1 (001 — screenshot do ChatGPT) |
| Telas de referência de design | 9 |

### 8.2 Componentes globais (aparecem em ≥ 2 telas distintas)
Card de plano · badge/pílula · CTA em pílula · lista de features com check · mockup de iPhone · card de feature com ilustração · avatar stack · navbar de landing · card de tarefa (versão em mockup).

### 8.3 Componentes exclusivos
- 001: modal `Add files`, sidebar de chat, bloco de código "Plain text", barra `Ask ChatGPT`.
- 006: widget de métricas com escudo.
- 012: accordion horizontal de cards numerados; grade de fundo.
- 014: placeholders de imagem e wireframe cinza; seção `User guide` com passos; seção `Services` com card invertido.
- 016: card de tarefa com faixa de estágio, contadores e moldura de "placa".
- 018: formulário de pagamento, `Upcoming Bills`, lista/accordion de benefícios, toggle `Monthly/Yearly`, carrossel de depoimentos, gráfico de rosca e sparkline.
- 004: countdown de lançamento e capa promocional com logos Webflow/Framer/Figma.

### 8.4 Modais e overlays
1 — modal `Add files` (001/017). Nenhum outro.

### 8.5 Formulários
- 004: e-mail + `JOIN WAITLIST`.
- 018: pagamento (`We're paying for`, `Pay with`, cartão, validade, CVC) e transferência (`Send Money`).
- 001: campo de busca `Search library`.

### 8.6 Tabelas
Nenhuma tabela de dados. Listas em formato de linha: `Upcoming Bills` (018), lista de benefícios (018), lista `Recents` (001).

### 8.7 Estados diferentes encontrados
- Overlay aberto (001) e item em loading/skeleton (001)
- Card destacado/recomendado (002, 010, 018)
- Item expandido vs colapsado (012; benefício em 018)
- Item concluído esmaecido (008 `User Testing`)
- Card invertido/ativo (014 `01 Furniture Design`)
- Toggle/segmented (018)
- Nenhum estado de erro, vazio ou sucesso explícito

### 8.8 Possíveis fluxos
- Assinar plano: pricing (002/010/018) → checkout (não presente) `[INFERIDO]`
- Entrar em lista de espera: 004 e-mail → confirmação (não presente) `[INFERIDO]`
- Pagar/transferir: 018 formulário → confirmação (não presente) `[INFERIDO]`
- Anexar arquivos: 001 modal → conversa `[INFERIDO]`

### 8.9 Telas semelhantes
- Pricing: 002 ≈ 010 ≈ seção de 018.
- Features em grade: 004 (seção 2) ≈ 008 ≈ 018 (2×2).
- Mockups de "My tasks": 004 ≈ 008 (mesma origem visual `[INFERIDO]`).
- Estrutura de landing: 014 ≈ ordem de seções de 018.

### 8.10 Telas que parecem variações de estado
**Nenhuma.** Todos os pares com sufixo " 2" são cópias byte a byte; não há variações de estado entre imagens do conjunto. (Variações de estado ocorrem *dentro* de imagens, como o card expandido em 012.)

### 8.11 Divergências nome × conteúdo
| Arquivo | O nome sugere | O conteúdo é |
|---|---|---|
| `04_View-onbarding-tutorial` | tutorial de onboarding | widget Privacy Report do Safari |
| `07_view-store-select` | seleção de loja | seção de landing "We've orchestrated Intelligence." |
| `06_view-move-select-card` | mover/selecionar card | pricing de 3 planos |
| `02_Viewcard-open` | card aberto | pricing de 2 planos |
| `10_viewcard-group.JPG.PNG` | grupo de cards | screenshot do ChatGPT (cópia de `01_View-group.PNG`) |
| `03_View_inforgraficacomercialsotre` | infográfico comercial | pôster de template Nearo |

Ao reconstruir a partir deste documento, **use o conteúdo** (seções 5–6), não os nomes de arquivo.

### 8.12 Erros de grafia preservados do original
`Comign Soon Website` (004) · `Naero` vs `Nearo` (004) · `Enterprice` (002) · `Produtis App` vs `Produtis`/`Products` `[INCERTO]` (004, 008) · `Get Start` (018, 2 ocorrências).

---

## 9. Apêndice — Especificações de handoff observadas

> Complementa o documento com o formato de `/design-handoff`. **Limite:** as imagens são exportações raster, sem tokens nem medidas oficiais. Medidas são estimativas; nomes de token abaixo são **propostos** (`[INFERIDO]`), não existentes nas imagens. Cores "amostradas" vêm dos pixels (±3 níveis por compressão).

### 9.1 Cores amostradas (tokens propostos)
| Token proposto | Valor | Origem | Uso |
|---|---|---|---|
| `color-canvas-neutral` | `#F2F3F5` | 002 | fundo da seção de pricing |
| `color-canvas-design-tool` | `#EBEBEB` | 016 | fundo do canvas de design |
| `color-surface-card` | `#FFFFFF` | 002, 006, 010, 016 | cards |
| `color-surface-muted` | `#F2F2F2` | 006 (tiles) | tiles de métrica |
| `color-surface-page` | `#F2F1F6` | 006 | fundo iOS |
| `color-badge-dark` | `#292E32` | 002 | badge `POPULAR` |
| `gradient-cta-personal` | `#C1D576` → `#F79935` | 002 | CTA Personal |
| `gradient-cta-business` | `#3CBEF0` → `#2FF6F9` → `#7EE4B2` | 002 | CTA Business |
| `color-stage-onboarding` | `#4AB3F7` | 016 | faixa `ON BOARDING` |
| `color-success-shield` | `#65C466` | 006 | ícone de escudo |
| `color-poster-bg` | `#ABC0D1` | 004 | fundo da capa |
| `color-hero-blue-base` | `#86C4ED` | 004 | base do hero |
| `color-section-neutral` | `#F7F7F7` | 004 | seção features |
| `color-frame-neutral` | `#E1E5E8` / `#ECF0F3` | 008 | moldura / cards |
| `color-outer-slate` | `#89929B` | 008 | fundo externo |
| `color-canvas-light` | `#F8F8F8` | 012 | fundo da seção |

### 9.2 Raios, sombras, espaçamento (estimados)
| Token proposto | Valor estimado | Onde |
|---|---|---|
| `radius-card-lg` | 28–40 px | 002, 006, 016 |
| `radius-card-md` | 20 px | 004 hero, 008 cards, 006 tiles |
| `radius-pill` | 999 px | CTAs, badges, navbar 018 |
| `shadow-card` | difusa, y≈8–24, blur≈24–48, opacidade baixa | 002, 010, 016 |
| `spacing-card-padding` | ≈ 32–36 px (2× em 1200 px de largura) | 002 |
| `spacing-feature-gap` | ≈ 20–24 px entre itens | 002 |

### 9.3 Tipografia (visual, sem fontes confirmadas)
| Uso | Aparência | Nota |
|---|---|---|
| Título de plano (002) | sans humanista, ~28 px | Lato-like `[INCERTO]` |
| Preço (002) | sans bold ~52 px + unidade ~16 px | — |
| H1 hero (004, 018) | grotesca clara/medium, 56–72 px | Inter/Helvetica-like `[INCERTO]` |
| Marca em plano (010) | sans bold + serif itálica | par de fontes |
| Título serifado (008) | serif de display | — |
| Chip mono (012) | monoespaçada caixa-alta | — |

### 9.4 Props propostas (componentes principais)
| Componente | Props | Notas |
|---|---|---|
| `PricingCard` | `name`, `price`, `period`, `tagline`, `features[]{title, description?}`, `cta{label, href}`, `badge?`, `highlighted?`, `accent` | `accent` define gradiente de borda/CTA (002) |
| `TaskCard` | `stageLabel`, `stageColor`, `title`, `description`, `assignees[]`, `status`, `counts{comments, links, files}`, `dueDate` | descrição truncada em 2 linhas (016) |
| `Badge` | `text`, `variant` (`dark`, `blue`, `soft-green`, `priority`) | — |
| `PhoneMockup` | `screen`, `floatingCards[]`, `fadeBottom` | ilustração |
| `FileSheet` (001) | `items[]`, `selectedIds[]`, `loading` | grade 3 col. |
| `AccordionCards` (012) | `items[]{number, icon, title, body, image?}`, `activeIndex` | 1 ativo |

### 9.5 Estados e interações (só o que é observável)
| Elemento | Estado | Comportamento observado / inferido |
|---|---|---|
| Card de plano | destacado | maior, borda/badge (002, 010, 018) |
| CTA | default | hover/active/disabled [INCERTO] |
| Card 012 | expandido vs colapsado | expansão de largura e conteúdo `[INFERIDO]` |
| Benefício 018 | expandido | descrição + underline azul |
| Modal 001 | aberto | fundo esmaecido; itens `Recent`; skeleton em 1 item |
| Item de tarefa (008) | concluído | check verde, texto esmaecido |
| Toggle 018 | `Monthly/Yearly` | alterna preço `[INFERIDO]` |

### 9.6 Responsividade
- **Observado:** apenas 014 mostra desktop e mobile lado a lado (wireframe). Não há breakpoints numéricos nas imagens.
- **Proposto `[INFERIDO]`:** cards de plano empilham em coluna única no mobile; grade 2×2 vira 1 coluna; navbar 018 colapsa em menu; countdown 004 mantém 4 colunas menores.

### 9.7 Edge cases (a especificar; não aparecem nas imagens)
- Descrição de card longa → truncar em 2 linhas com reticências (observado em 016).
- Nomes de arquivo longos → truncar com reticências (observado em 001).
- Textos internacionais mais longos em CTAs em pílula → definir largura mínima e `nowrap`.
- Estados vazio/erro/loading: só há skeleton em 001; demais [INCERTO].

### 9.8 Movimento
Nenhuma animação observável (imagens estáticas). Sugestões para futura especificação `[INFERIDO]`: expansão de card 012, transição de destaque em pricing, contagem regressiva em 004.

### 9.9 Acessibilidade
- Contraste: textos cinza claros sobre branco em descrições (002, 010, 016) devem ser verificados contra WCAG AA `[INCERTO]`.
- Ícones sem rótulo visível (012, 016 contadores) exigem `aria-label`.
- Ordem de foco sugerida em pricing: nome → preço → features → CTA.
- Toggle `Monthly/Yearly` e segmented `Card/Bank Account` devem usar `role="tablist"`/`radiogroup` conforme semântica.
- Countdown (004) deve ter `aria-live="off"` e alternativa textual para data-alvo.