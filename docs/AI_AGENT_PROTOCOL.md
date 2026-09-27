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

## Proibições

- Não alterar a semântica de um ID publicado.
- Não usar o mesmo ID para tipos diferentes.
- Não transformar fases, documentos ou ferramentas em domínios funcionais.
- Não inserir produtos `Mxx` como filhos de domínios `Dxx`.
- Não declarar aprovação, owner ou evidência inexistente.

## Saída esperada do agente

Relate os arquivos alterados, a razão da mudança, o resultado da validação e qualquer lacuna que permaneça como `proposed`.
