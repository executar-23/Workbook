# Prompt executável — Reclassificação de insumos no esquema GM01–GM06

> Preparado em modo `transform` (executar-prompt): não executado agora, para
> ser invocado depois. Ao rodar, siga literalmente as seções abaixo.

## OBJECTIVE

Adicionar a camada `grupo_macro` (GM01–GM06) acima de `Axx` no registry e
propagar essa classificação para as 85 entradas de
`evidence/master_index.yaml`, produzindo:
1. `architecture.yaml#macro_areas[].grupo_macro` preenchido para as 13 macroáreas.
2. Uma nova coluna `grupo_macro` em `evidence/master_index.yaml` e
   `evidence/master_index.csv`, derivada por `Dxx → primary_area (Axx) → GMxx`.
3. `python scripts/validate.py` continuando a passar sem alterar a contagem
   de IDs além do necessário (nenhum ID de evidência é renumerado).

## CONTEXT

<context>
O usuário forneceu esta árvore-alvo do Workbook (superior a `Axx/Dxx`):

```
WORKBOOK
├── I. CONTROLE E NAVEGAÇÃO
├── II. ARQUITETURA E CAPACIDADES
│   ├── GM01 Estratégia, Governança e Corporativo
│   ├── GM02 Negócio, Mercado e Growth
│   ├── GM03 Produto e Experiência
│   ├── GM04 Engenharia, Plataforma e Operações
│   ├── GM05 Dados, Conhecimento e Documentação
│   └── GM06 Execução, Automação e Ferramentas
│       └── A00–A12 → D01–D23 → Subdomínios
├── III. PORTFÓLIO, OPERAÇÃO E GOVERNANÇA
│   ├── Portfólio · Control Plane · Governança
└── IV. CONHECIMENTO E CONTINUIDADE
    ├── Documentos · Agentes · Alertas · Próximas ações · Corpus
```

`GM01–GM06` é uma camada **nova**, ainda não existe em `registry/`. As seções
I, III e IV **não são domínio de conteúdo** — já correspondem 1:1 a partes
existentes do registry (ver tabela em CONSTRAINTS); não were re-derivadas por
insumo, só documentadas como referência para quem for montar o
`WORKBOOK_INTEGRADO.html` depois.

Estado atual do repositório (`executar-23/Workbook`, branch a partir de
`main`):
- `registry/session_a/architecture.yaml` tem 13 `macro_areas` (`A00`–`A12`) e
  23 `domains` (`D01`–`D23`), cada domínio com `primary_area` já preenchido.
- `evidence/master_index.yaml` tem 85 entradas (81 arquivos físicos + 4
  registros `duplicado`/`historico` sem arquivo próprio), cobrindo os
  domínios D06, D07, D09, D10, D11, D12, D13, D16, D17, D18, D20, D21, D23.
  Todas já têm campo `dominio: Dxx` preenchido — a reclassificação é uma
  **derivação mecânica**, não uma nova leitura de conteúdo.
- `docs/ID_CONVENTIONS.md` documenta o padrão `Dxx-EVID-nnn` (evidência de
  intake); precisa ganhar uma linha para `GMnn` quando este prompt rodar.
</context>

## INPUT

<input>
- `registry/session_a/architecture.yaml` (macro_areas + domains, fonte da
  verdade de `Axx`/`Dxx`/`primary_area`)
- `evidence/master_index.yaml` (85 entradas, campo `dominio` já preenchido)
- Mapeamento `Axx → GMxx` proposto pelo usuário (ver CONSTRAINTS) — não
  inventar outro; se o usuário quiser mudar, é decisão humana antes de rodar.
</input>

## CONSTRAINTS

- Obrigatório: usar exatamente este mapeamento `Axx → GMxx` (cobre as 13
  macroáreas, nenhuma sobra):

  | GM | Nome | Axx |
  |---|---|---|
  | GM01 | Estratégia, Governança e Corporativo | A00, A07, A12 |
  | GM02 | Negócio, Mercado e Growth | A01, A08 |
  | GM03 | Produto e Experiência | A02, A03 |
  | GM04 | Engenharia, Plataforma e Operações | A04, A05 |
  | GM05 | Dados, Conhecimento e Documentação | A06, A10 |
  | GM06 | Execução, Automação e Ferramentas | A09, A11 |

- Obrigatório: `grupo_macro` de um domínio/evidência = `grupo_macro` do seu
  `primary_area` (`Axx`) — nunca do `supporting_areas`.
- Obrigatório: preservar todos os `Dxx-EVID-nnn`, `SRC-nn` e IDs existentes;
  esta é uma coluna nova, não uma renumeração (ver `governance.id_migrations`
  se algo precisar mudar de ID — não deveria ser necessário aqui).
- Obrigatório: `status: proposed` no que for adicionado — `grupo_macro` é uma
  taxonomia nova ainda sem aprovação humana formal, mesmo sendo mecânica.
- Proibição: não reclassificar o campo `dominio` (`Dxx`) de nenhuma entrada
  — isso já foi decidido nos lotes anteriores; este prompt só adiciona a
  camada acima, não revisita a de baixo.
- Proibição: não criar arquivos novos em `evidence/` nem tocar em
  `registry/session_a/documents.yaml` (37 documentos canônicos, fora de
  escopo).
- Limite: seções I, III e IV da árvore-alvo **não** recebem reclassificação
  de insumo neste prompt — são apenas documentadas (ver tabela abaixo) para
  não se perderem, não fazer merge automático de conteúdo nelas.

  | Seção da árvore | Já corresponde a |
  |---|---|
  | I. Controle e Navegação | `docs/NAVIGATION.md`, `AGENTS.md`, `docs/AI_AGENT_PROTOCOL.md`, `master_index.yaml#transversal_pattern` |
  | III. Portfólio | `registry/session_a/portfolio.yaml` |
  | III. Control Plane | `registry/session_a/master_index.yaml` (seção SA-06) |
  | III. Governança | `registry/session_a/governance.yaml` |
  | IV. Documentos | `registry/session_a/documents.yaml` |
  | IV. Agentes | `registry/session_b/objects.yaml` (tipo `AGT`) |
  | IV. Alertas | `governance.yaml` / master_index SA-10 |
  | IV. Próximas ações | master_index SA-11 |
  | IV. Corpus | `evidence/` (este próprio diretório) |

## TOOLS

- `Read`/`Grep` → ler `architecture.yaml` e `evidence/master_index.yaml`
  antes de editar; confirmar que a contagem de entradas/domínios não mudou
  desde este prompt (se mudou, recontar antes de aplicar o mapeamento).
- `Edit` → adicionar `grupo_macro: GMxx` em cada `macro_areas[]` de
  `architecture.yaml`, e `grupo_macro: GMxx` em cada `entries[]` de
  `evidence/master_index.yaml` (só nas que têm `dominio` preenchido).
- `Bash` (`python3`) → regenerar `evidence/master_index.csv` a partir do
  YAML atualizado (mesmo padrão dos scripts anteriores desta sessão); rodar
  `python scripts/validate.py` ao final.
- `Write` → atualizar `docs/ID_CONVENTIONS.md` (nova linha `GMnn`) e
  `evidence/README.md` (nova coluna na tabela de cobertura).

## EXECUTION

1. Ler `architecture.yaml#macro_areas` e confirmar as 13 entradas `A00`–`A12`.
2. Para cada macroárea, adicionar `grupo_macro: GMxx` conforme a tabela em
   CONSTRAINTS. Não alterar `id`, `name`, `status`, `source_refs`.
3. Ler `evidence/master_index.yaml#entries`. Para cada entrada com `dominio`
   preenchido, resolver `primary_area` do domínio (via `architecture.yaml`)
   e então `grupo_macro` (via a tabela). Adicionar o campo `grupo_macro` na
   entrada.
4. Entradas `duplicado`/`historico` sem `caminho` próprio herdam o
   `grupo_macro` do `dominio` que já têm — não pular.
5. Atualizar `total_entries`/contadores de `domain_coverage` só se a
   contagem de arquivos mudou (não deveria mudar neste prompt).
6. Regenerar `evidence/master_index.csv` com a nova coluna `grupo_macro`
   (entre `dominio` e `dominio_nome`, ou ao final — manter todas as colunas
   existentes).
7. Adicionar em `docs/ID_CONVENTIONS.md` uma linha para `GMnn` (Grupo Macro,
   escopo `architecture.yaml#macro_areas` e `evidence/`), citando que é
   camada nova acima de `Axx`.
8. Atualizar `evidence/README.md`: nova coluna `Grupo Macro` na tabela de
   cobertura por domínio, e uma nota curta citando a tabela de
   correspondência I/III/IV do CONSTRAINTS (sem duplicar o conteúdo, só
   referenciar).
9. Rodar `python scripts/validate.py`. Se falhar, corrigir antes de seguir —
   não commitar com validação vermelha.
10. Comitar (`feat: add GM01-06 grupo_macro layer above Axx in registry and
    evidence`), push na branch atual, e abrir PR (draft) seguindo o mesmo
    padrão dos PRs anteriores desta sessão (#3, #4, #5).

## OUTPUT CONTRACT

- `registry/session_a/architecture.yaml`: 13/13 macroáreas com
  `grupo_macro` preenchido, sem nenhum outro campo alterado.
- `evidence/master_index.yaml` e `.csv`: todas as entradas com `dominio`
  preenchido também têm `grupo_macro`; nenhuma entrada perdida ou duplicada;
  contagem total de entradas idêntica à anterior (85, salvo se novos
  insumos tiverem entrado entretanto — recontar antes).
- `docs/ID_CONVENTIONS.md` e `evidence/README.md` atualizados.
- Resumo final ao usuário: quantas entradas ganharam cada `GMxx`, e
  confirmação de que `validate.py` passou.

## VALIDATION

- `python scripts/validate.py` → `OK: ...` sem erro.
- `python3 -c "import yaml; d=yaml.safe_load(open('registry/session_a/architecture.yaml')); assert all('grupo_macro' in a for a in d['macro_areas'])"` sem erro.
- `python3 -c "import yaml; d=yaml.safe_load(open('evidence/master_index.yaml')); assert all(('grupo_macro' in e) for e in d['entries'] if e.get('dominio'))"` sem erro.
- Soma de entradas por `GMxx` no CSV bate com a soma de entradas por `Dxx`
  agrupadas pela tabela de CONSTRAINTS (checagem cruzada manual de 2–3
  domínios).

## STOP CONDITIONS

Finalizar quando `validate.py` passar, as 85 entradas (ou a contagem atual,
se mudou) tiverem `grupo_macro`, os dois arquivos de documentação estiverem
atualizados, e o PR estiver aberto. Não expandir para gerar o
`WORKBOOK_INTEGRADO.html` nem para reclassificar `dominio` — isso é fora do
escopo deste prompt.
