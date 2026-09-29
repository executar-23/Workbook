# CLAUDE.md — instruções de sessão para este repositório

Leia primeiro `AGENTS.md` — fonte da verdade do protocolo de agentes deste
repositório (ordem de leitura, fluxo `sync → inspect → change → validate →
commit → sync`, convenção de IDs, separação Sessão A × Sessão B). Este
arquivo só acrescenta a regra abaixo, específica de **como o Workbook é
escrito**; não substitui nem repete o resto do protocolo.

## Construção e população do Workbook

- O Workbook (edição legível — Partes `WB-P1`/`WB-P2`/`WB-P3`, 17 páginas
  `WB-H01`–`WB-H17` já especificadas em
  `registry/session_a/workbook_manual.yaml#html_edition`) é construído e
  populado **diretamente em `README.md`**, na raiz do repositório. Não gerar
  um `WORKBOOK_INTEGRADO.html` nem qualquer outro arquivo separado para o
  corpo do documento — `README.md` é o próprio Workbook.
- **Proibido usar deep links ou hiperlinks dentro do corpo do Workbook**:
  nenhum `[texto](#ancora)`, `[texto](arquivo.md)` ou `<a href>` entre
  páginas/seções do documento. Referência a outro ID (`Dxx`, `WB-Hnn`,
  `SRC-nn`, `Dxx-EVID-nnn`...) fica como texto plano ("ver WB-H05"), nunca
  como link clicável — um agente de IA localiza pelo ID via busca textual,
  não precisa de navegação clicável. Essa proibição é só para a navegação
  *interna* do Workbook; um link de URL externa fora do corpo do documento
  (ex.: em "Validação"/instruções técnicas) não é afetado.
- **Cada parte é uma página**: bloco delimitado por um cabeçalho de página
  (ID, título, mapeamento `WB-Pn`, status) e uma linha de fechamento visual
  (separador `---`) antes da próxima. "Página" aqui é unidade lógica de
  conteúdo, não paginação de impressão real — Markdown não pagina.
- **Índice legível por agente**: `README.md` mantém, logo após a capa, um
  ÍNDICE em tabela plana (ID · nome · mapeamento · status · última
  atualização), sem links. O índice **deve ser atualizado no mesmo commit**
  que adicionar, editar ou mudar o status de qualquer página — nunca
  deixar o índice divergir do conteúdo. Antes de finalizar uma edição de
  página, conferir e corrigir a linha correspondente do índice.
- Nada aqui substitui `AGENTS.md`/`docs/AI_AGENT_PROTOCOL.md`:
  `status: proposed`, `TBD` para lacunas, e `python scripts/validate.py`
  antes de cada commit continuam obrigatórios. Popular uma página com
  conteúdo inventado (sem fonte em `registry/`/`evidence/`) é proibido —
  lacuna vira `TBD`, nunca texto genérico.
