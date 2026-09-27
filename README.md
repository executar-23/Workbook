# Workbook EXECUTAR

Fonte canônica, versionada e legível por máquina do Master Schema do ecossistema EXECUTAR (GOV-WORKBOOK-001), separando:

- **Sessão A — Consulta / Knowledge System** (`registry/session_a/`): o que o sistema é e conhece.
- **Sessão B — Produção / Execution System** (`registry/session_b/`): como o sistema executa, sempre referenciando IDs da Sessão A.

## Estrutura

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

## Validação

```bash
pip install -r requirements.txt
python scripts/validate.py
```

Toda alteração mantém IDs estáveis, referências válidas, separação capacidades × portfólio e Sessão A × Sessão B. Lacunas são `TBD`.
