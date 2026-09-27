# Protocolo operacional para agentes de IA

## Objetivo

Manter um único modelo confiável do ecossistema EXECUTAR, adequado para automação, documentação e auditoria.

## Classificação antes de editar

Classifique cada item em exatamente um tipo principal:

| Tipo | Prefixo | Uso |
|---|---|---|
| Macroárea | `Axx` | Agrupamento de capacidades |
| Domínio | `Dxx` | Capacidade funcional permanente |
| Programa | `Pxx` | Coordenação estratégica do portfólio |
| Produto ou iniciativa | `Mxx` | Trabalho que consome capacidades |
| Gate | `Gxx` | Ponto formal de decisão |
| Fonte | `SRC-xx` | Evidência de origem |
| Documento canônico | `Dxx-DOC-ACR-nnn` | Artefato da Sessão A |
| Seção Master Index / Foundation | `SA-nn` / `SB-nn` | Navegação Sessão A / B |
| Objeto de produção | `CYC` `SPR` `TSK` `ISS` `RB` `AGT` `CMD` `EDL` … | Sessão B (ver `docs/ID_CONVENTIONS.md`) |
| Conflito / lacuna / decisão | `CNF` / `GAP` / `DEC` | Governança |

Subdomínios, workflows, procedimentos, entregáveis, ADRs e requisitos devem usar `SD`, `WF`, `SOP`, `E`, `ADR` e `REQ`, com IDs qualificados pelo pai quando forem adicionados.

## Regras de alteração

1. Pesquise o ID, o nome e sinônimos antes de criar um registro.
2. Prefira relacionar entidades existentes a criar duplicatas.
3. Trate `primary_area` como classificação principal; use `supporting_areas` para relações transversais.
4. Declare dependências por ID. Nunca dependa apenas de nomes livres.
5. Use `status: proposed` para conteúdo ainda não aprovado.
6. Acrescente uma fonte em `sources` quando houver evidência verificável.
7. Para corrigir um ID, preserve o anterior em `governance.id_migrations`.
8. Execute a validação antes de registrar a mudança.

## Sessão A × Sessão B

- Conhecimento (definição, estrutura, campos, regra) vive **só** na Sessão A.
- Objeto da Sessão B precisa de `refs_a` com ≥1 ID existente da Sessão A e não pode conter `sections`, `record_schema`, `definition` ou `purpose_canonical` (o validador bloqueia).
- Forma de runbook/linha editorial é herdada por `shape_ref`, nunca copiada.

## Modelo epistêmico (SRC-03)

Todo valor preenchido declara `epistemic_class` (DIRECT, DERIVED, EXTERNAL_EVIDENCE, PROPOSED, GAP, CONFLICT, HYPOTHESIS) e `source_refs`. Ausente = `TBD`. Derivação exige ≥2 evidências compatíveis e justificativa. Proposta vai em `proposed_value`; o canônico continua `TBD`. Nunca reproduza segredos.

Controle de estado: documento encontrado ≠ completo ≠ aprovado; código ≠ implementado; deploy ≠ verificado; asset ≠ publicado; plano ≠ resultado. Documentos param em `PRE_PREENCHIDO`; aprovação é ato humano.

## Execução

- WIP = 1 por agente; processe domínios em ordem D01 → D23 quando o trabalho for por corpus (`WF-PREFILL-001`).
- Divergência sem supersessão explícita → registre `CNF-nnn`; nunca escolha em silêncio.
- Pergunte ao humano só o que não pode ser obtido, pesquisado ou derivado; agrupe em `USER_ACTION_REQUIRED`.

## Proibições

- Não alterar a semântica de um ID publicado.
- Não usar o mesmo ID para tipos diferentes.
- Não transformar fases, documentos ou ferramentas em domínios funcionais.
- Não inserir produtos `Mxx` como filhos de domínios `Dxx`.
- Não declarar aprovação, owner ou evidência inexistente.
- Não criar `Mxx` para frentes sem fonte (ver GAP-001…005).
- Não criar instâncias da Sessão B sem `refs_a`.

## Saída esperada do agente

Relate os arquivos alterados, a razão da mudança, o resultado da validação e qualquer lacuna que permaneça como `proposed`.
