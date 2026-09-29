# Prompt executável (reutilizável) — popular uma área do Workbook em `README.md`

> Preparado em modo `transform` (executar-prompt): não executado agora.
> Invocar depois, uma vez por área (`{AREA}`), repetindo este mesmo
> arquivo — nunca editar duas áreas na mesma execução (WIP=1).

## OBJECTIVE

Popular em `README.md` a(s) página(s) `WB-Hnn` cobertas por `{AREA}`
(um `GMxx` — ex. `GM01` — ou um `Dxx` dentro dele), com o conteúdo
disponível em `registry/`/`evidence/`, e recalcular no mesmo turno o
ÍNDICE e o PAINEL DE COMPLETUDE — sem tocar em nenhuma outra página.

## CONTEXT

<context>
Este prompt é a continuação operacional de `CLAUDE.md` (regra-mãe: o
Workbook vive só em `README.md`, sem deep link/hiperlink interno, cada
parte é uma "página" com cabeçalho+fechamento, índice atualizado no
mesmo commit) e de `evidence/RECLASSIFICACAO_GM01-06.prompt.md` (camada
`GM01–GM06` já aplicada em `architecture.yaml` e `evidence/master_index.yaml`).

Objetivo de produto do usuário: `README.md` não é só o documento final —
é o **painel de controle e acompanhamento de completude** do Workbook,
atualizado dia a dia, uma área por vez, em texto plano com tabelas
(sem HTML), até convergir num resultado final para impressão.

Fontes de dado por página, nesta ordem de prioridade:
1. `registry/session_a/*.yaml` — conteúdo já canônico (playbooks,
   contratos, portfólio, governança) para a área.
2. `evidence/master_index.csv`/`.yaml` filtrado por `grupo_macro`/`dominio`
   igual a `{AREA}` — insumo bruto (`Dxx-EVID-nnn`), ainda `status:
   proposed`, mas é a melhor evidência disponível quando o registry
   estiver vazio/TBD.
3. Nenhuma das duas → campo fica `TBD`. Nunca inventar.

Mapeamento fixo `WB-Hnn → WB-Pn` (não mudar, fonte:
`registry/session_a/workbook_manual.yaml#html_edition.parts`):
WB-H01 Visão Executiva·WB-P1 · WB-H02 Governança·WB-P1 · WB-H03 Cadeia de
Valor·WB-P1 · WB-H04 Áreas do Ecossistema·WB-P2 · WB-H05 Portfólio·WB-P1 ·
WB-H06 Planejamento·WB-P3 · WB-H07 Roteiro de Evolução·WB-P3 · WB-H08
Ciclos de Trabalho·WB-P3 · WB-H09 Processos·WB-P2 · WB-H10 Interfaces
entre Áreas·WB-P2 · WB-H11 Dados e Fontes Principais·WB-P1 · WB-H12
Documentos e Evidências·WB-P1 · WB-H13 Riscos Problemas e Bloqueios·WB-P3
· WB-H14 Indicadores·WB-P1 · WB-H15 Painel Executivo·WB-P3 · WB-H16
Lacunas e Decisões Pendentes·SA-10 · WB-H17 Rastreabilidade·SA-00.

Mapeamento `GMxx → Axx` (fixo, `architecture.yaml#macro_areas[].grupo_macro`):
GM01=A00,A07,A12 · GM02=A01,A08 · GM03=A02,A03 · GM04=A04,A05 ·
GM05=A06,A10 · GM06=A09,A11.

`WB-Hnn` não mapeia 1:1 para `GMxx` (mapeia para `WB-Pn`, que é
transversal). Ao popular uma página, filtrar dentro dela apenas o
conteúdo cujo domínio/área pertence à `{AREA}` pedida; o restante da
página continua `TBD`/`vazio` até a área correspondente ser processada
numa execução futura deste mesmo prompt.
</context>

## INPUT

<input>
- `{AREA}`: um `GMxx` (ex. `GM03`) ou um `Dxx` dentro dele (ex. `D10`).
- Estado atual de `README.md` (CAPA, ÍNDICE, PAINEL DE COMPLETUDE e
  páginas já existentes).
</input>

## CONSTRAINTS

- Obrigatório: WIP=1 — uma única `{AREA}` por execução. Não adiantar
  outra área "de brinde".
- Obrigatório: nenhum campo populado sem fonte rastreável
  (`registry/session_a/*.yaml#caminho` ou `Dxx-EVID-nnn`). Lacuna = `TBD`,
  nunca texto genérico ou "a definir" sem o marcador `TBD`.
- Obrigatório: toda página segue o esqueleto fixo (ver EXECUTION passo 3)
  — mesmo cabeçalho/fechamento em toda execução, de qualquer dia, para
  não fragmentar o formato do documento.
- Obrigatório: corpo da página em tabela Markdown (`| campo | valor |`)
  sempre que o dado for tabular; texto corrido só quando não couber em
  tabela (ex. narrativa de resumo executivo).
- Obrigatório: recalcular ÍNDICE e PAINEL DE COMPLETUDE no mesmo commit
  — nunca deixar `%`/status desatualizado.
- Obrigatório: `%` de completude = `páginas com status "populado" ÷ 17`
  (contagem mecânica, nunca estimativa).
- Proibição: nenhum `[texto](#ancora)`, `[texto](arquivo.md)` ou
  `<a href>` dentro do corpo do Workbook (herda de `CLAUDE.md`).
- Proibição: não editar página fora de `{AREA}`; não tocar `registry/`
  a menos que a própria área exija promover um item de `evidence/` a
  canônico — e nesse caso, tratar como decisão humana separada (parar e
  perguntar), não como parte automática deste prompt.
- Limite: se `{AREA}` já teve alguma página iniciada por execução
  anterior, completar/corrigir essa página em vez de recriar do zero.

## TOOLS

- `Read`/`Grep` → ler `README.md` atual, `registry/session_a/*.yaml` e
  `evidence/master_index.csv` filtrado por `{AREA}` antes de escrever
  qualquer linha.
- `Edit` → editar `README.md`: a página da área, a linha do ÍNDICE, o
  bloco do PAINEL DE COMPLETUDE. Nunca reescrever o arquivo inteiro
  quando um `Edit` cirúrgico resolve.
- `Bash` (`python3`) → recalcular a contagem de páginas populadas (evitar
  contar manualmente e errar); rodar `python scripts/validate.py` antes
  de commitar.

## EXECUTION

1. Resolver o escopo de `{AREA}`: se for `GMxx`, listar os `Axx` (tabela
   em CONTEXT) e os `Dxx` cujo `primary_area` cai nesse `GMxx`
   (`architecture.yaml#domains[].primary_area`); se for `Dxx`, usar
   direto. Determinar quais `WB-Hnn` podem receber conteúdo dessa área
   (qualquer página cujo tema toque esses domínios — nem toda página
   recebe conteúdo de toda área).
2. Reunir insumo: para cada `Dxx` do escopo, ler as entradas de
   `evidence/master_index.csv` com esse `dominio`, e o conteúdo canônico
   já existente em `registry/session_a/domain_contracts.yaml`/
   `documents.yaml` para o mesmo `Dxx`.
3. Para cada página `WB-Hnn` afetada, escrever/atualizar o bloco no
   esqueleto fixo:
   ```
   ## WB-Hnn · <Nome da página> — Página
   `mapeamento: WB-Pn` · `status: <status>` · `atualizado: <AAAA-MM-DD>`

   <corpo: tabela(s) Markdown com os campos populados desta área;
   campos de outras áreas ainda não processadas permanecem "TBD">

   --- fim da página WB-Hnn ---
   ```
   `status` = `populado` só quando **todas** as áreas que a página cobre
   já tiverem sido processadas; enquanto faltar alguma, `status:
   rascunho`.
4. Atualizar a linha do ÍNDICE para cada `WB-Hnn` tocada (coluna Status +
   Última atualização).
5. Recalcular o PAINEL DE COMPLETUDE (bloco novo, logo após o ÍNDICE, se
   ainda não existir):
   ```
   ### Painel de Completude
   Progresso: N/17 páginas populadas (XX%)

   | Grande Macro | Páginas WB-H afetadas | Status |
   |---|---|---|
   | GM01 Estratégia, Governança e Corporativo | WB-H02, WB-H16, WB-H17 | ... |
   | GM02 Negócio, Mercado e Growth | ... | ... |
   | GM03 Produto e Experiência | ... | ... |
   | GM04 Engenharia, Plataforma e Operações | ... | ... |
   | GM05 Dados, Conhecimento e Documentação | ... | ... |
   | GM06 Execução, Automação e Ferramentas | ... | ... |
   ```
   `N` = contagem mecânica (`Bash`/`python3`) de páginas com `status:
   populado` no ÍNDICE, nunca digitado de cabeça.
6. Rodar `python scripts/validate.py`. Corrigir antes de seguir se falhar.
7. Commitar (`docs: popular {AREA} no Workbook (WB-Hnn, ...)`), push,
   PR (draft) — mesmo padrão dos PRs anteriores deste repositório.

## OUTPUT CONTRACT

- Só `README.md` alterado (a menos que uma promoção formal a canônico
  tenha sido explicitamente pedida e confirmada pelo usuário — então
  também o arquivo de `registry/` correspondente).
- Diff contém: o(s) bloco(s) de página de `{AREA}`, a(s) linha(s) do
  ÍNDICE tocadas, o PAINEL DE COMPLETUDE recalculado. Nenhuma outra
  página/linha muda.
- Resumo final ao usuário: quais `WB-Hnn` mudaram de status, novo `%`
  geral, e quais campos ficaram `TBD` por falta de fonte.

## VALIDATION

- Toda página tocada tem cabeçalho + linha de fechamento no formato fixo.
- Nenhuma página fora de `{AREA}` foi alterada (`git diff` mostra só os
  blocos esperados).
- Cada linha do ÍNDICE reflete o `status` real da página correspondente.
- `%` do Painel = contagem mecânica, confere com o número de páginas
  `populado` no ÍNDICE.
- `grep` confirma ausência de `[texto](#`, `[texto](arquivo.md)` ou
  `<a href` em `README.md`.
- `python scripts/validate.py` → `OK`.

## STOP CONDITIONS

Finalizar quando toda página afetada por `{AREA}` estiver com `status:
populado` (ou `rascunho` explícito, se a página também depende de outra
área ainda não processada), o ÍNDICE e o Painel de Completude
refletirem isso, e o PR estiver aberto. Não avançar para a próxima área
sem um novo pedido explícito do usuário invocando este prompt de novo.
