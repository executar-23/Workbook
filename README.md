# Workbook EXECUTAR

Este `README.md` é o próprio Workbook — capa, índice e as 17 páginas
`WB-H01`–`WB-H17` são construídas e populadas aqui, conforme
`CLAUDE.md#construção-e-população-do-workbook`. Sem deep links nem
hiperlinks entre páginas; IDs são texto plano, localizáveis por busca.

---

## CAPA

| Campo | Valor |
|---|---|
| ID | `GOV-WORKBOOK-001` |
| Título | Sistema Integrado de Governança e Operação EXECUTAR |
| Versão | `1.1.0` (`registry/workbook.yaml#schema_version`) |
| Data da consolidação | 2026-09-27 (`registry/workbook.yaml#metadata.updated_at`) |
| Situação documental | `proposed` |
| Período coberto | TBD (sem fonte) |

---

## ÍNDICE

Tabela plana, sem links. Localizar uma página pelo ID via busca textual no
próprio arquivo (ex.: buscar `WB-H05`). Atualizar esta tabela no mesmo
commit que adicionar, editar ou mudar o status de qualquer página —
conferir esta regra em `CLAUDE.md` antes de fechar a edição.

| ID | Nome | Mapeamento | Status | Última atualização |
|---|---|---|---|---|
| WB-H01 | Visão Executiva | WB-P1 | vazio — aguardando população | — |
| WB-H02 | Governança | WB-P1 | vazio — aguardando população | — |
| WB-H03 | Cadeia de Valor | WB-P1 | vazio — aguardando população | — |
| WB-H04 | Áreas do Ecossistema | WB-P2 | vazio — aguardando população | — |
| WB-H05 | Portfólio | WB-P1 | vazio — aguardando população | — |
| WB-H06 | Planejamento (estratégico/tático/operacional) | WB-P3 | vazio — aguardando população | — |
| WB-H07 | Roteiro de Evolução (agora/próximo/futuro) | WB-P3 | vazio — aguardando população | — |
| WB-H08 | Ciclos de Trabalho | WB-P3 | vazio — aguardando população | — |
| WB-H09 | Processos | WB-P2 | vazio — aguardando população | — |
| WB-H10 | Interfaces entre Áreas | WB-P2 | vazio — aguardando população | — |
| WB-H11 | Dados e Fontes Principais | WB-P1 | vazio — aguardando população | — |
| WB-H12 | Documentos e Evidências | WB-P1 | vazio — aguardando população | — |
| WB-H13 | Riscos Problemas e Bloqueios | WB-P3 | vazio — aguardando população | — |
| WB-H14 | Indicadores | WB-P1 | vazio — aguardando população | — |
| WB-H15 | Painel Executivo | WB-P3 | vazio — aguardando população | — |
| WB-H16 | Lacunas e Decisões Pendentes | SA-10 | vazio — aguardando população | — |
| WB-H17 | Rastreabilidade | SA-00 | vazio — aguardando população | — |

Fonte da lista de páginas: `registry/session_a/workbook_manual.yaml#html_edition.parts`.
Nenhuma página tem conteúdo ainda — este commit só formata capa e índice.

---

## Sobre este repositório

Fonte canônica, versionada e legível por máquina do Master Schema do ecossistema EXECUTAR (GOV-WORKBOOK-001), separando:

- **Sessão A — Consulta / Knowledge System** (`registry/session_a/`): o que o sistema é e conhece.
- **Sessão B — Produção / Execution System** (`registry/session_b/`): como o sistema executa, sempre referenciando IDs da Sessão A.

### Estrutura

| Caminho | Conteúdo |
|---|---|
| `registry/workbook.yaml` | Raiz: metadata, contrato de agentes, includes, convenções de IDs |
| `registry/session_a/master_index.yaml` | Master Index SA-00…SA-12 + padrão transversal |
| `registry/session_a/architecture.yaml` | A00–A12, D01–D23, subdomínios e entregáveis |
| `registry/session_a/domain_contracts.yaml` | Playbook (21 campos) + Interface Contract por domínio |
| `registry/session_a/documents.yaml` | 37 documentos canônicos (23 macro + 14 especializados) |
| `registry/session_a/portfolio.yaml` | P00, M0–M16, frentes do ecossistema |
| `registry/session_a/governance.yaml` | Gates, estados, modelo epistêmico, fontes, conflitos, gaps, decisões |
| `registry/session_a/workbook_manual.yaml` | Partes I–III, matriz fractal, L0–L6, edição HTML |
| `registry/session_a/pm_lifecycle.yaml` | PM01–PM13 |
| `registry/session_b/*.yaml` | Foundation Doc SB-00…11, fluxo do ciclo, tipos/instâncias de objetos |
| `schema/workbook.schema.yaml` | JSON Schema do documento consolidado |
| `scripts/validate.py` | Schema + integridade referencial + regra B→A |
| `docs/` | Arquitetura, IDs, navegação, protocolo de agentes |
| `assets/design-system/` | Tokens + componentes da edição HTML do Workbook (WB-H01–H17), deliverable `D21-E01` — `status: proposed` |
| `evidence/` | Insumo bruto classificado por domínio (`Dxx-EVID-nnn`) e grupo macro (`GMnn`), aguardando promoção humana |

### Validação

```bash
pip install -r requirements.txt
python scripts/validate.py
```

Toda alteração mantém IDs estáveis, referências válidas, separação capacidades × portfólio e Sessão A × Sessão B. Lacunas são `TBD`.
