# Regras para agentes de IA

## Fonte da verdade

Leia, nesta ordem:

1. `AGENTS.md`
2. `docs/AI_AGENT_PROTOCOL.md`
3. `docs/ARCHITECTURE.md`, `docs/ID_CONVENTIONS.md`, `docs/NAVIGATION.md`
4. `schema/workbook.schema.yaml`
5. `registry/workbook.yaml` e `registry/session_a/master_index.yaml`

`registry/` (raiz `registry/workbook.yaml` + `session_a/` + `session_b/`) é a fonte canônica. Textos explicativos não podem redefinir IDs ou relações.

## Fluxo obrigatório

Use o ciclo `sync -> inspect -> change -> validate -> commit -> sync`.

- Mudanças pequenas e atômicas (regra de branch: ver CNF-007).
- Atualize o repositório antes de editar.
- Preserve mudanças recentes de outros agentes.
- Interrompa se houver conflito sem resolução determinística.
- Execute `python scripts/validate.py` antes de cada commit.
- Não renumere nem reutilize IDs existentes.
- Registre substituições em `governance.id_migrations`.
- Produtos `Mxx` consomem capacidades `Axx/Dxx`; não os aninhe na árvore funcional.
- Não crie entidades, relações, responsáveis, estados ou evidências sem fonte; use TBD.
- Objetos da Sessão B sempre com `refs_a` para IDs da Sessão A.

## Critério de conclusão

Uma mudança só está concluída quando o YAML é válido, todas as referências existem, a validação passa e a documentação afetada foi atualizada.
