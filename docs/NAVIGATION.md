# Dependências e regras de navegação

## Ordem de consulta
1. `registry/session_a/master_index.yaml` → seção SA pertinente.
2. Contexto funcional: `Axx` → `Dxx` (`architecture.yaml`) → contrato (`domain_contracts.yaml`) → documentos (`documents.yaml`).
3. Contexto de produto: `Mxx` (`portfolio.yaml`) → `consumes_areas/consumes_domains` → volta ao passo 2.
4. Execução: `session_b/foundation.yaml` (SB-xx) → `refs_a` → Sessão A. Nunca o contrário: Sessão A não referencia instâncias da Sessão B.

## Direção das arestas permitidas
```
Mxx ──consome──▶ Axx / Dxx          Dxx ──parent──▶ Axx
Dxx ──documents──▶ Dxx-DOC-*        Dxx-DOC-* ──depends_on/blocks──▶ Dxx-DOC-*
Objeto B ──refs_a──▶ qualquer ID A  Objeto B ──shape_ref──▶ Dxx-DOC-* (forma herdada, não copiada)
Fluxo B: CYC → OBJ → RDM → BKL → SPR → TSK/ISS → Gate(Gnn) → KPI → Learning → CYC
```

## Dependências entre documentos
`depends_on`/`blocks` existem em todos os documentos e estão vazios (nenhuma fonte define). Preencher somente com evidência.

## Resolução de conflito
Precedência de fontes em `governance.yaml#epistemic_model.source_precedence`. Divergência sem supersessão explícita → novo `CNF-nnn`; nunca escolher em silêncio.

## Estados
Registry: `proposed/active/deprecated/archived`. Documentos: `implementation_states` (terminam em PRE_PREENCHIDO sem evidência). Trabalho B: `official_states`; CONCLUÍDO = execução + resultado + verificação + evidência.
