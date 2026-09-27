# 02 — AGENT INDEX
## EXECUTAR · Gestão de Projetos × TDAH

**Root bundle:** `EXECUTAR-ADHD-PM-CANONICAL-001`  
**Machine source:** `01_YAML_BUNDLE.yaml`  
**Purpose:** permitir que agentes consultem, rastreiem e reutilizem os dois DOCX sem perder diferenças, origem ou estado epistemológico.

## 1. Regra de entrada do agente

1. Carregue `bundle_manifest`.
2. Resolva a consulta por `canonical_id`.
3. Leia primeiro a entidade canônica.
4. Para validação, citação ou divergência, siga `source_refs`.
5. Para reconstrução integral, use `source_archive`.
6. Nunca complete `TBD` sem nova fonte incorporada.
7. Não trate decisão de produto (`E`) como conclusão clínica/científica.

## 2. IDs raiz

| ID | Tipo | Uso |
|---|---|---|
| `DATA-ADHD-PM-001` | Pesquisa | Registro mestre da matriz Gestão de Projetos × TDAH |
| `DRIVE-PROD-002` | Operação | Registro/verificação do schema CSV |
| `SCHEMA-MATRIZ-GESTAO-TDAH-V1` | Contrato | Campos registrados para a matriz |
| `MATRIX-GP-ADHD-001` | Dataset canônico | 11 linhas `GP-01..GP-11` |
| `HYPOTHESIS-SET-001` | Governança de evidência | Hipóteses e estado após pesquisa |
| `ARCH-COMPENSATORY-001` | Arquitetura | Operação humana → assistência do sistema |
| `EPISTEMIC-GOV-001` | Governança | Classes, cautelas e regras epistemológicas |
| `GP-CHAIN-001` | Taxonomia operacional | Cadeia detalhada de funções de gestão |
| `PM-RESPONSIBILITIES-001` | Responsabilidades | `PM-01..PM-08` |
| `HUM-CAP-001` | Capacidades | Capacidades humanas/operacionais |
| `TAX-ADHD-PM-001` | Taxonomia | Termos de indexação |

## 3. Hierarquia operacional

```text
EXECUTAR-ADHD-PM-CANONICAL-001
├── DATA-ADHD-PM-001
│   ├── SCHEMA-MATRIZ-GESTAO-TDAH-V1
│   ├── MATRIX-GP-ADHD-001
│   │   ├── GP-01 ... GP-11
│   │   └── HYPOTHESIS-SET-001
│   └── ARCH-COMPENSATORY-001
├── DRIVE-PROD-002
├── DOMAIN MODEL
│   ├── GP-CHAIN-001
│   ├── GP-FUNC-01 ... GP-FUNC-04
│   ├── PM-01 ... PM-08
│   ├── HUM-CAP-001
│   └── TAX-ADHD-PM-001
├── EPISTEMIC-GOV-001
└── SOURCE ARCHIVE
    ├── SRC-PMI-TDHA-EVID-20260821
    └── SRC-ADM-20260821
```

## 4. Matriz canônica `GP-01..GP-11`

| ID | Núcleo |
|---|---|
| `GP-01` | Iniciação e escopo |
| `GP-02` | Planejamento |
| `GP-03` | Priorizar e sequenciar |
| `GP-04` | Cronograma e prazos |
| `GP-05` | Iniciar execução |
| `GP-06` | Execução |
| `GP-07` | Monitorar execução e progresso |
| `GP-08` | Detectar desvios e adaptar |
| `GP-09` | Comunicação e stakeholders |
| `GP-10` | Finalização e avaliação |
| `GP-11` | Capacidade e forecasting |

Cada linha contém demanda de gestão, capacidade humana exigida, vulnerabilidade associada ao TDAH, fonte clínica, fonte científica, função executiva, classe de evidência, impacto, mecanismo/consequência, compensação e conclusão de produto/design.

## 5. Dependências e rastreabilidade

```text
DRIVE-PROD-002
      │ registers_schema_for
      ▼
DATA-ADHD-PM-001
      │
      ├── SCHEMA-MATRIZ-GESTAO-TDAH-V1 ── structures ──► MATRIX-GP-ADHD-001
      │                                                       │
      │                                                       ├── GP-01..GP-11
      │                                                       └── HYPOTHESIS-SET-001
      │
      └──────────────────────────────────────────────────────► ARCH-COMPENSATORY-001
```

**Sintaxe de origem**
- Parágrafo: `SRC-...:p:123`
- Faixa: `SRC-...:p:123-130`
- Tabela: `SRC-...:t:2`
- Linha de tabela: `SRC-...:t:2:r:5`

## 6. Regras epistemológicas críticas

`C` é explicitamente descrito na fonte como **Publicado**. `E` é explicitamente descrito como **Inferido**. A classe `B` aparece, mas sua definição não é explicitada nos dois arquivos; portanto permanece `TBD`.

A fonte sustenta investigar arquitetura que externalize parte das operações executivas, mas não sustenta universalizar déficits para toda pessoa com TDAH nem afirmar ganho mensurável de produtividade sem teste empírico.

## 7. Conteúdo exclusivo preservado

**Fonte `SRC-PMI-TDHA-EVID-20260821`:**
- `DRIVE-PROD-002`;
- registro do `SCHEMA_MATRIZ_GESTAO_TDAH_V1.csv`;
- estado documental/epistemológico do CSV;
- classificação final publicada/inferida e claim ainda não verificado.

**Fonte `SRC-ADM-20260821`:**
- diagrama-base função de gestão × TDAH → impacto → produto;
- taxonomia adicional;
- cadeia detalhada de 18 funções de gestão;
- `GP-FUNC-01..04`;
- capacidades de `SEC-005`;
- responsabilidades `PM-01..PM-08`.

## 8. Campos que o agente não deve inventar

- `Owner`: não determinado.
- `Projeto`: não determinado.
- definição da classe epistemológica `B`: `TBD`.
- separação exata de `impacto_operacional_mecanismo` e `impacto_operacional_consequencia`: a tabela original os combina; o bundle preserva o texto bruto.
- referências bibliográficas completas/URLs: não estão integralmente disponíveis.
- conteúdo do CSV registrado: o arquivo é mencionado, mas não foi fornecido.
- conteúdo dos documentos `JSON AEVO`, `HOJE > Preencher(1).md`, `SEC-002`, `SEC-004`, `SEC-005`: apenas referências internas aparecem nos DOCX.

## 9. Protocolo de consulta recomendado

**Pergunta sobre uma função específica:** resolver `GP-xx` → retornar dados da linha → validar `source_refs`.  
**Pergunta sobre arquitetura:** abrir `ARCH-COMPENSATORY-001` → cruzar com `GP-xx` relevantes → verificar `HYPOTHESIS-SET-001`.  
**Pergunta sobre evidência:** abrir `EPISTEMIC-GOV-001` → usar somente o que a matriz/fonte declara → não extrapolar.  
**Pergunta sobre conteúdo original:** ir diretamente a `source_archive` pelo locator.  
**Nova fonte:** adicionar `source_id`, hash, locators e relações; nunca sobrescrever o histórico anterior.
