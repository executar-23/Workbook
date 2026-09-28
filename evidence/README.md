# Evidência de intake (fora do `registry/`)

Insumo bruto importado de um export da conta claude.ai (categoria `projects`,
2026-09-28), organizado pela mesma taxonomia de domínios `D01–D23` já canônica
em `registry/session_a/architecture.yaml`. Ver `master_index.yaml` /
`master_index.csv` para o índice completo.

## O que é / o que não é

- `registry/` é schema-validado e fechado em 37 documentos canônicos (23 MACRO
  + 14 SPECIALIZED). Estes 73 arquivos **não são** documentos canônicos novos —
  são evidência/insumo bruto para eventualmente preencher ou informar
  documentos existentes (ex.: os 6 arquivos `D16-DOC-*` aqui dentro são
  **candidatos** a preencher os documentos já registrados `D16-DOC-PEM-001` e
  correlatos — não os substituem automaticamente).
- Cada arquivo recebeu um ID novo, `Dxx-EVID-nnn` (documentado em
  `docs/ID_CONVENTIONS.md`), só válido dentro de `evidence/`.
- `doc_class` de cada entrada segue as classes já definidas em
  `workbook_manual.yaml#html_edition.parts` (WB-H12): `evidencia` (padrão) ou
  `duplicado` (conteúdo idêntico a outro arquivo do mesmo lote — sem arquivo
  físico próprio, só a entrada no índice apontando para o principal).
- Tudo com `status: proposed`. Nada aqui foi aprovado, revisado ou promovido.

## Origem (fontes)

- `SRC-08` — projeto Claude "27-09-WORKBOOK" (46 arquivos únicos)
- `SRC-09` — projeto Claude "Eu-26-27" + arquivo de memória `career-ai-europe.md`
  (13 arquivos, todos em `D17_emprego-portfolio/`)
- `SRC-10` — projeto Claude "HANDOFF-STORE" (14 arquivos únicos)

Registradas em `registry/session_a/governance.yaml#sources`, mesmo padrão do
`SRC-07` (handoff): um `SRC-nn` por lote de origem, não um por arquivo.

Fora de escopo nesta rodada (confirmado com o usuário): as demais categorias do
mesmo export — `conversations`, `design_chats`, `frames`, `light_metadata` —
são histórico de conta/conversa, não documentos de projeto, e não foram
ingeridas.

## Classificação por domínio

| Domínio | Nome | Arquivos |
|---|---|---|
| D06 | Conhecimento e Busca | 17 |
| D07 | Produtividade e Execução | 2 |
| D10 | Gestão de Produto | 2 |
| D11 | Experiência e Projeto | 10 |
| D12 | Engenharia | 2 |
| D13 | Mercado e Demanda | 2 |
| D16 | Mídias e Comunicação | 15 |
| D17 | Emprego e Portfólio | 13 |
| D18 | Contratos e Esquemas | 1 |
| D20 | Plataformas e Repositórios | 1 |
| D21 | Workbook | 6 |
| D23 | Blueprints | 2 |

D01–D05, D08, D09, D14, D15, D19, D22 não receberam arquivo neste lote — isso
não é uma lacuna (`GAP-nnn`), só ausência de insumo nesta importação.

Duas entradas têm classificação marcada como ambígua em `master_index.yaml`
(nota `ambiguo:`) — mantidas na classificação mais defensável, sujeitas a
revisão humana:
- `D06-EVID-016` (equipe-aquisicao-retencao-experiencia): poderia ser D04
  Pessoas e RH; ficou em D06 por pertencer à série de conhecimento `AIKB-*`.
- `D16-EVID-011` (risco-cognitivo.html): poderia ser D09 Pesquisa e Inovação;
  ficou em D16 por ser a landing editorial pública do produto, não pesquisa.

## Normalização de arquivo

Arquivos sem extensão no export (`Contexto`, `Prompt`, `tokens`…) foram salvos
como `.md`. Arquivos cujo nome original era `.docx`/`.rtf` mas cujo conteúdo
exportado é só o texto extraído (sem marcação binária) foram salvos como
`.md` com o sufixo `__extraido` no nome, para não sugerir que são um arquivo
Office/RTF de verdade. Formatos já nativamente texto (`.md`, `.txt`, `.csv`,
`.json`, `.yaml`, `.html`) mantiveram a extensão original.

## Próximos passos (não automáticos)

- Revisão humana das 2 classificações ambíguas acima.
- Decidir, arquivo por arquivo, quais dos 6 `D16-DOC-*` aqui promovem conteúdo
  para os documentos canônicos já registrados em `documents.yaml` (isso exige
  edição campo a campo dentro do schema existente — não um merge automático).
- `Eu-26-27` (D17) contém dados pessoais (nome completo, decisões de carreira)
  — commit autorizado explicitamente pelo usuário; sem essa autorização este
  material não deveria ir para um repositório compartilhado.
