# Como operar este Workbook — guia prático para outro agente

## 1. Leia nesta ordem antes de tocar em qualquer arquivo
1. `AGENTS.md` — protocolo geral do repositório (fluxo, IDs, Sessão A×B).
2. `CLAUDE.md` — regra específica do Workbook: ele vive **só** em
   `README.md`, sem deep link/hiperlink interno, cada parte é uma
   "página" com cabeçalho+fechamento, índice sempre sincronizado.
3. `README.md` — estado atual: CAPA, ÍNDICE (17 páginas `WB-H01`–
   `WB-H17`), Painel de Completude, e as páginas já escritas.
4. `docs/prompts/POPULAR_AREA_WORKBOOK.prompt.md` — o prompt operacional
   que você vai executar.

## 2. Entenda a hierarquia (não é preciso memorizar, só saber onde consultar)
```
Workbook → Grande Macro (GM01–GM06) → Macroárea (A00–A12) → Domínio (D01–D23) → Subdomínio → Entregável → Documento
```
- Fonte da verdade: `registry/session_a/architecture.yaml`
  (`macro_areas[].grupo_macro`, `domains[].primary_area`).
- Mapa completo já está montado na página `WB-H04` do `README.md` —
  comece por lá para ver o quadro geral, não recalcule do zero.
- Insumo bruto (ainda não canônico) está em
  `evidence/master_index.yaml`/`.csv`, classificado por `dominio` (`Dxx`)
  e `grupo_macro` (`GMxx`).

## 3. Regra de ouro: WIP = 1 área por execução
Nunca popule duas áreas (`GMxx` ou `Dxx`) na mesma rodada — exceção:
páginas puramente estruturais (como `WB-H04`), que não dependem de
evidência e por isso saem completas de uma vez.

## 4. Passo a passo para popular uma área
1. Peça/confirme qual `{AREA}` (ex.: `GM02` ou `D13`) você vai atacar.
2. Abra `docs/prompts/POPULAR_AREA_WORKBOOK.prompt.md` e siga a seção
   `EXECUTION` literalmente:
   - Resolver quais `Axx`/`Dxx` a área cobre.
   - Reunir insumo: `evidence/master_index.csv` filtrado por essa área +
     `registry/session_a/documents.yaml`/`domain_contracts.yaml` para o
     que já é canônico.
   - Escrever/editar a(s) página(s) `WB-Hnn` afetadas usando o esqueleto
     fixo (cabeçalho com ID/nome/mapeamento/status/data, corpo em tabela
     Markdown, linha de fechamento).
   - Atualizar a linha correspondente no ÍNDICE.
   - Recalcular o Painel de Completude (contagem mecânica — nunca de
     cabeça).
3. **Nunca inventar.** Campo sem fonte em `registry/` ou `evidence/`
   fica `TBD`, texto plano — nunca uma frase genérica.
4. Rodar `python scripts/validate.py` — se falhar, corrigir antes de
   continuar.
5. Conferir com `grep` que não entrou nenhum `[texto](#...)`,
   `[texto](arquivo.md)` ou `<a href` no `README.md`.
6. Commit descrevendo exatamente qual área/páginas mudaram, push na
   branch, abrir PR (draft) — mesmo padrão dos PRs anteriores deste
   repositório (título claro, corpo com resumo + test plan).

## 5. Checklist de aceite antes de finalizar
- [ ] Só a(s) página(s) da área pedida mudou(aram) — nenhuma outra
      página foi tocada.
- [ ] ÍNDICE reflete o status real de cada página tocada.
- [ ] Painel de Completude recalculado (N/17 e % corretos).
- [ ] Sem link/deep-link interno no `README.md`.
- [ ] `python scripts/validate.py` → `OK`.

## 6. O que NUNCA fazer
- Popular mais de uma área por execução.
- Promover conteúdo de `evidence/` a canônico em `registry/` sem pedido
  humano explícito.
- Renumerar ou reutilizar qualquer ID (`Dxx`, `WB-Hnn`, `GMxx`,
  `SRC-nn`...).
- Deixar o índice ou o painel desatualizados em relação ao conteúdo
  real.
