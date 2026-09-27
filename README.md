# Workbook EXECUTAR

Fonte canônica, versionada e legível por máquina para a arquitetura de governança do ecossistema EXECUTAR.

## Estrutura

- `schema/workbook.schema.yaml`: contrato formal e regras de validação.
- `registry/workbook.yaml`: registro canônico de macroáreas, domínios e portfólio.
- `docs/AI_AGENT_PROTOCOL.md`: procedimento obrigatório para agentes de IA.
- `scripts/validate.py`: validação local do registro.

## Validação

```bash
python scripts/validate.py
```

Toda alteração deve manter IDs estáveis, referências válidas e separação entre capacidades permanentes e produtos do portfólio.
