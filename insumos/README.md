# insumos/ — inbox de material bruto

Esta pasta **não é** `registry/` (canônico, validado por `scripts/validate.py`) nem o "Corpus Detalhado" tratado de SA-12. É o **inbox**: material bruto recebido, preservado no formato original, ainda **não processado**.

## O que tem aqui

| Pasta | Origem | Conteúdo |
|---|---|---|
| `AI-CORPUS-UNIFICADO/` | `AI_CORPUS_UNIFICADO.zip` | 16 documentos `AIKB-0001…0016` + `README_AI.md` + `INDEX_AI.txt` + `MANIFEST_AI.jsonl` (manifesto próprio, com sha256 por arquivo). Governança editorial, arquitetura do blog/creator economy, topologia técnica, agentes de IA, schema AI-native, estratégia editorial e framework "Risco Cognitivo". |
| `EXECUTAR-ADHD-PM-CANONICAL-BUNDLE/` | `EXECUTAR_ADHD_PM_CANONICAL_BUNDLE.zip` | `01_YAML_BUNDLE.yaml` + `02_AGENT_INDEX.md`. Corpus de pesquisa canônico (Gestão de Projetos × TDAH), com namespace de IDs próprio (`DATA-`, `MATRIX-GP-01..11`, `HYPOTHESIS-`, `ARCH-COMPENSATORY-001`…) — **não** usa IDs Axx/Dxx/Mxx do Workbook. |
| `EXECUTAR-BLOG-LANCAMENTO-FULLSTACK/` | `EXECUTAR-BLOG-LANCAMENTO-FULLSTACK.bundle.yaml` | Bundle de 1.047 campos já estruturado no formato do contrato de campo do Workbook (`Dxx-DOC-ACR-nnn.SECAO.CAMPO`, `classe_epistemica`, `status_fonte`, `confianca`), cobrindo D01–D23 (núcleo/condicional) em 8 fases F00–F07, declarado para `M2` (Executar Blog). Fonte primária declarada no próprio arquivo: uma planilha `EXECUTAR_HUB_Control_Plane_v2.xlsx` que **não** foi enviada. |
| `RISCO-COGNITIVO-HUB-EDITORIAL-CMS/` | `Risco_Cognitivo_Hub_Editorial_CMS_v1.0.xlsx` | Planilha CMS com 22 abas (design system, dashboard, banco de conteúdo, brief, mapa de argumentos, evidências, produção de texto, ativos derivados, infográficos, YouTube, shorts, social, newsletter, SEO, calendário, distribuição, performance, backlog, taxonomia, config, log de decisões). |

Ver `SOURCE_REGISTER.yaml` para o inventário formal (id `INS-nnn`, hash, relação sugerida, status).

## Regras para o agente que for processar isto

1. **Nenhum arquivo aqui altera `registry/` automaticamente.** Promover conteúdo para o registry é um ato de execução do workflow `WF-PREFILL-001` (`registry/session_b/execution_flow.yaml`), cujo primeiro passo (`PF-00`) é justamente inventariar fontes — este `SOURCE_REGISTER.yaml` é esse inventário inicial.
2. Um item só vira uma fonte canônica `SRC-nn` quando registrado em `registry/session_a/governance.yaml#sources`, com `location` apontando para o caminho dentro de `insumos/`.
3. A "relação sugerida" na tabela acima e no `SOURCE_REGISTER.yaml` **não é vínculo formal** — é uma leitura de primeira leitura, sujeita a confirmação durante o prefill (mesma cautela que o próprio bundle do Blog já registra: "a planilha não vincula formalmente os 37 artefatos ao M2").
4. `EXECUTAR-ADHD-PM-CANONICAL-BUNDLE/` tem seu próprio protocolo de consulta e proibições em `02_AGENT_INDEX.md` (seção "Campos que o agente não deve inventar") — respeitar antes de citar qualquer conteúdo dele.
5. Arquivos `.docx`/`.rtf`/`.xlsx` exigem a skill correspondente (docx/xlsx) para leitura estruturada; não foram convertidos aqui para preservar o formato original tal como recebido.
6. Nunca preencher lacuna com conhecimento genérico: seguir o modelo epistêmico já definido em `registry/session_a/governance.yaml#epistemic_model` (DIRECT/DERIVED/EXTERNAL_EVIDENCE/PROPOSED/GAP/CONFLICT) e marcar `TBD` quando não houver evidência.

## Próximo passo

Executar `WF-PREFILL-001` por domínio (D01 → D23, WIP=1), usando estes insumos como fonte, registrando `source_refs` em cada campo preenchido e promovendo fontes usadas para `SRC-07`, `SRC-08`… em `governance.yaml`.
