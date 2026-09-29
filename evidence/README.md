# Evidência de intake (fora do `registry/`)

Insumo bruto de três lotes — (1) export da conta claude.ai, categoria
`projects`, 2026-09-28; (2) e (3) dois uploads diretos de 5 arquivos cada,
2026-09-29 — organizado pela mesma taxonomia de domínios `D01–D23` já
canônica em `registry/session_a/architecture.yaml`. Ver `master_index.yaml` /
`master_index.csv` para o índice completo.

## O que é / o que não é

- `registry/` é schema-validado e fechado em 37 documentos canônicos (23 MACRO
  + 14 SPECIALIZED). Estes 81 arquivos **não são** documentos canônicos novos —
  são evidência/insumo bruto para eventualmente preencher ou informar
  documentos existentes (ex.: os 6 arquivos `D16-DOC-*` aqui dentro são
  **candidatos** a preencher os documentos já registrados `D16-DOC-PEM-001` e
  correlatos — não os substituem automaticamente).
- Cada arquivo recebeu um ID novo, `Dxx-EVID-nnn` (documentado em
  `docs/ID_CONVENTIONS.md`), só válido dentro de `evidence/`.
- `doc_class` de cada entrada segue as classes já definidas em
  `workbook_manual.yaml#html_edition.parts` (WB-H12): `evidencia` (padrão),
  `duplicado` (conteúdo idêntico a outro arquivo do mesmo lote — sem arquivo
  físico próprio, só a entrada no índice apontando para o principal) ou
  `historico` (versão anterior de um arquivo que foi atualizado por outro —
  mantido, nunca apagado).
- Arquivos `.docx`/`.xlsx` cujo binário real foi enviado (não apenas texto
  extraído) são mantidos como binário — nenhuma extração/conversão lossy.
- Tudo com `status: proposed`. Nada aqui foi aprovado, revisado ou promovido.

## Origem (fontes)

- `SRC-08` — projeto Claude "27-09-WORKBOOK" (46 arquivos únicos)
- `SRC-09` — projeto Claude "Eu-26-27" + arquivo de memória `career-ai-europe.md`
  (13 arquivos, todos em `D17_emprego-portfolio/`)
- `SRC-10` — projeto Claude "HANDOFF-STORE" (14 arquivos únicos)
- `SRC-11` — upload direto de 5 arquivos (2026-09-29, lote 2): 3 novos (manual
  da skill RC Domain Expert OS, planilha GTM atualizada, "Ecossistema\_.html"
  — um workbook reader integral) + 2 que já existiam idênticos no lote
  `SRC-08` (`EXECUTAR_projetosaasentrypoint_EXPANDIDO.schema.json` e
  `EXECUTAR_Foundation_Doc_GTM_Blog.md`, mesmo hash SHA1 — registrados como
  `duplicado` no índice, sem novo arquivo físico).
- `SRC-12` — upload direto de 5 arquivos (2026-09-29, lote 3): matriz PMI×TDAH
  (`D09-EVID-001`), matriz ADM-26 função-de-gestão×déficit-TDAH
  (`D09-EVID-002`), PRD do motor adaptativo de execução do Projeto EXECUTAR
  (`D10-EVID-003`), atualização v013 do knowledge pack `RC-KNW-001`
  (`D06-EVID-019`, supera `D06-EVID-001` v01 — mantido como `historico`) e o
  dashboard de evidência governada TDAH×Framework 694 (`D06-EVID-020`).

Registradas em `registry/session_a/governance.yaml#sources`, mesmo padrão do
`SRC-07` (handoff): um `SRC-nn` por lote de origem, não um por arquivo.

Fora de escopo nesta rodada (confirmado com o usuário): as demais categorias do
mesmo export — `conversations`, `design_chats`, `frames`, `light_metadata` —
são histórico de conta/conversa, não documentos de projeto, e não foram
ingeridas.

## Classificação por domínio

| Domínio | Nome | Grupo Macro | Arquivos |
|---|---|---|---|
| D06 | Conhecimento e Busca | GM05 | 20 |
| D07 | Produtividade e Execução | GM06 | 2 |
| D09 | Pesquisa e Inovação | GM05 | 2 |
| D10 | Gestão de Produto | GM03 | 3 |
| D11 | Experiência e Projeto | GM03 | 10 |
| D12 | Engenharia | GM04 | 2 |
| D13 | Mercado e Demanda | GM02 | 3 |
| D16 | Mídias e Comunicação | GM02 | 15 |
| D17 | Emprego e Portfólio | GM01 | 13 |
| D18 | Contratos e Esquemas | GM05 | 1 |
| D20 | Plataformas e Repositórios | GM06 | 1 |
| D21 | Workbook | GM05 | 7 |
| D23 | Blueprints | GM05 | 2 |

D01–D05, D08, D14, D15, D19, D22 não receberam arquivo em nenhum lote — isso
não é uma lacuna (`GAP-nnn`), só ausência de insumo nas importações até agora.

## Grupo Macro (GM01–GM06)

Camada nova acima de `Axx`, adicionada em `architecture.yaml#macro_areas[].grupo_macro`
e propagada a cada entrada de `master_index.yaml`/`.csv` via `Dxx → primary_area
(Axx) → GMnn` (tabela fixa em `RECLASSIFICACAO_GM01-06.prompt.md#CONSTRAINTS`).
`status: proposed` como todo o resto — camada mecânica, não revisada por humano.

| Grupo Macro | Nome | Entradas |
|---|---|---|
| GM01 | Estratégia, Governança e Corporativo | 13 |
| GM02 | Negócio, Mercado e Growth | 19 |
| GM03 | Produto e Experiência | 14 |
| GM04 | Engenharia, Plataforma e Operações | 2 |
| GM05 | Dados, Conhecimento e Documentação | 33 |
| GM06 | Execução, Automação e Ferramentas | 4 |

As seções `I. Controle e Navegação`, `III. Portfólio/Operação/Governança` e
`IV. Conhecimento e Continuidade` da árvore-alvo do Workbook não são domínio
de insumo — já correspondem a arquivos existentes do registry (`portfolio.yaml`,
`governance.yaml`, `documents.yaml`, `objects.yaml`, `evidence/` como Corpus);
ver a tabela completa em `RECLASSIFICACAO_GM01-06.prompt.md#CONSTRAINTS`.

Três entradas têm classificação marcada como ambígua em `master_index.yaml`
(nota `ambiguo:`) — mantidas na classificação mais defensável, sujeitas a
revisão humana:
- `D06-EVID-016` (equipe-aquisicao-retencao-experiencia): poderia ser D04
  Pessoas e RH; ficou em D06 por pertencer à série de conhecimento `AIKB-*`.
- `D16-EVID-011` (risco-cognitivo.html): poderia ser D09 Pesquisa e Inovação;
  ficou em D16 por ser a landing editorial pública do produto, não pesquisa.
- `D09-EVID-002` (ADM-26-21-08): poderia ser D01 Gestão Empresarial ou D04
  Pessoas e RH; ficou em D09 por ser o par direto de `D09-EVID-001` (mesma
  matriz de evidência PMI×TDAH).

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
