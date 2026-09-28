ADR-001.md⁠￼

O ADR consolida a arquitetura, a legenda de migração, o fluxo, as contagens, os riscos e os critérios de implantação.

A nomenclatura principal ficou:

Conceito original	Nome adotado
VHM-P	Modelo de processo reutilizável
VHM-C	Configuração do cliente
HPG	Instância de processo configurada
HA	Operador humano responsável
HEP	Console operacional
FG / FB	Caminho principal / retorno e retrabalho
Orchestrator	Motor de workflow e agente executor

Seu conceito foi preservado: um padrão reutilizável, poucos controles humanos e automações configuradas por cliente. O motor controla estados, autorizações e retomadas; o agente executa tarefas delimitadas.

As contagens foram corrigidas:

* 43 derivados; chegar a 45 exige identificar duas saídas adicionais.
* 22 tarefas, cinco fases e cinco famílias de entregáveis são categorias distintas.
* 17 dias de preparação e 15 dias de publicação são janelas separadas, com sobreposição ainda por definir.
* 9, 8Δ e 17/Δ permanecem como referências históricas, sem funcionar como métricas operacionais.

A modelagem usa BPMN como referência; o desenho incluído é conceitual, não um processo executável. A supervisão e os controles de risco foram orientados pelo NIST AI RMF. 

Validação concluída: consistência conceitual e aritmética. A implantação ainda exige mapear os estados A/B/C/D e testar falhas, retomadas, isolamento entre clientes e prevenção de publicações duplicadas. ADR-001 — Automação configurável com supervisão humana

2026-09-24. Versão 1.0. Status: documentado; implantação condicionada.

Contexto. Padrão reutilizável, poucos controles, fluxos contínuos, IA e configuração por cliente.

Decisão. Compor modelo de processo versionado e configuração do cliente para criar uma instância. O motor de workflow persiste estados, autorizações e retomadas; o agente executa tarefas delimitadas através de ferramentas autorizadas. Instâncias terminam; novas demandas reiniciam. Retrabalho limitado.

Legenda. Nomes locais; não são siglas oficiais BPMN.

|Esboço          |Nomenclatura adotada                              |
|----------------|--------------------------------------------------|
|VHM-P           |Modelo de processo reutilizável                   |
|VHM-C           |Configuração do cliente                           |
|HPG             |Instância de processo configurada                 |
|HA / Human ADM  |Operador humano responsável                       |
|HEP / OS / US   |Console operacional e interfaces                  |
|A/B/C/D         |Estados dos dois controles; transições pendentes  |
|Orchestrator    |Motor de workflow + agente executor               |
|FG-01           |Caminho principal de execução                     |
|FB-1            |Caminho de retorno/retrabalho                     |
|FR / FE / GPR   |Execução e eventos de monitoramento               |
|Skills / plugins|Capacidades e ferramentas versionadas             |
|Conectores      |Adaptadores de integração autenticados            |
|Dependências    |Pré-condições e relações entre tarefas            |
|HADM / Δ        |Contagens legadas sem métrica operacional definida|

Modelagem. BPM é gestão de processos; BPMN é sua notação. Usar User Tasks para intervenção humana, Service Tasks para automação, gateways para decisões, eventos para início/fim/tempo, lanes para responsabilidades e message flows entre participantes distintos. Esquema conceitual, não BPMN executável.

flowchart TD
    E([Demanda]) --> C[Configurar e validar]
    C --> P[Produzir e derivar]
    P --> A{Aprovação humana}
    A -->|Aprovado| D[Agendar e publicar]
    A -->|Revisar dentro do limite| P
    A -->|Cancelar ou exceder limite| X([Encerrar e registrar])
    D --> M[Monitorar resultados]
    M --> X

Contagens validadas.

• Instância = configurar(modelo, cliente) substitui 1+1=3; o 3 não representa quantidade derivada.
• Inventário inicial: 1 humano, 1 console, 2 controles, 4 estados declarados, 1 agente, 2 caminhos. Categorias distintas, sem soma agregada.
• 9, 8Δ e 17/Δ ficam históricos, sem uso operacional.
• 22 tarefas: cadastrar IDs, responsáveis, entradas, saídas e dependências. Cinco fases propostas: configurar, produzir, derivar, validar, distribuir/monitorar. Ciclos configuráveis.
• Cinco famílias por ciclo: artigo, vídeo, imagens, quick frameworks, assets CTA. Pacotes não equivalem automaticamente a peças.
• 3+6+6+4+12+6+3+3=43. Total 45 exige identificar duas saídas adicionais distintas.
• 22+5+5=32 aritmeticamente; tarefas, fases e macros não constituem 32 tarefas.
• Preparação: 14+3=17 dias; publicação: janela separada de 15 dias. Definir calendário, início e sobreposição.
• Plataformas, formatos, skills, agentes, dependências: inventários separados; X indefinido.

Riscos e otimização. Aprovação antes da publicação; permissões mínimas; isolamento por cliente; conteúdo externo tratado como dados; deduplicação; retentativas limitadas; pausa/cancelamento; auditoria. Paralelizar somente tarefas independentes. Medir duração, custo, retrabalho e falhas por instância.

Consequências. Reuso e rastreabilidade; maior esforço de configuração. Rejeitados fluxos independentes por cliente e controle irrestrito pelo agente.

Aceite. Mapear estados e saídas; testar rejeição, retomada sem duplicação, indisponibilidade e isolamento. Validado conceitualmente/aritmeticamente; execução ainda não testada.

Referências: OMG BPMN 2.0.2; NIST AI RMF. Controles propostos pelo ADR.O próximo passo é criar um contrato de qualidade mensurável para o seu processo padrão. A fórmula permanece igual para todos os clientes; metas, escopo e limites são configurados por cliente.

Para desenhar e validar esse padrão, use DMADV: definir, medir, analisar, desenhar e verificar. Depois, use DMAIC para melhorar a operação existente: definir, medir, analisar, melhorar e controlar. Essa distinção é utilizada pela ASQ. 

Proponho um Índice de Qualidade Operacional — IQO, específico para seu sistema. É uma proposta de engenharia a validar, não uma fórmula oficial de BPM.

IQO = 100 \times G \times
\min\left(1,\frac{Q}{Q_{\text{meta}}},
\frac{P}{P_{\text{meta}}},
\frac{C_{\text{limite}}}{C_{\text{real}}}\right)

Variável	Definição por ciclo
Q	Entregas aprovadas sem retrabalho ÷ entregas previstas para o período
P	Entregas aprovadas dentro do prazo ÷ entregas previstas para o período
C_real	Custo total do ciclo ÷ entregas aprovadas
C_limite	Custo máximo acordado por entrega equivalente
G	1 quando os controles críticos passam; 0 quando há violação crítica

O custo inclui trabalho humano, execução tecnológica, retrabalho e manutenção atribuída ao cliente. Compare entregas equivalentes: um artigo e uma imagem não devem ser tratados automaticamente como unidades iguais.

O operador mínimo faz o índice acompanhar a dimensão com pior desempenho relativo. Economia não compensa atraso ou baixa qualidade.

Exemplo hipotético:

* Qualidade: 90%; meta: 95%.
* Pontualidade: 95%; meta: 95%.
* Custo por entrega: 125; limite: 100.
* Controles críticos atendidos: G = 1.

IQO = 100 \times \min(1;0{,}947;1;0{,}8)=80

Isso significa atendimento mínimo de 80% às metas, e não “80% de qualidade absoluta”. O custo é o principal desvio.

Como detectar complexidade improdutiva?

Registre separadamente integrações, regras específicas, intervenções manuais e exceções. Não penalize diretamente a quantidade: mais variáveis podem gerar valor. Investigue quando seu crescimento acompanha aumento de custo, retrabalho ou atraso, mantendo comparável o escopo.

Aplicação prática:

1. Definir critérios de aceite, metas e controles críticos antes do ciclo.
2. Instrumentar tarefas, aprovações, tempos, custos e exceções.
3. Executar um piloto e estabelecer a referência.
4. Comparar ciclos equivalentes e investigar desvios por componente.
5. Testar uma melhoria e medir seu efeito antes de incorporá-la ao padrão.

Sem dados suficientes, marque “não calculável”; nunca atribua nota máxima. Sem entregas aprovadas, classifique o ciclo como falha.

Mantenha os componentes visíveis junto ao número único. Indicadores compostos precisam de avaliação de sensibilidade para verificar se suas escolhas de cálculo produzem conclusões consistentes.  CQCA, nesta síntese: Contexto, Questão, Conclusão e Ação — interpretação provisória da sigla.

                 VISÃO SISTÊMICA
============================================================
[PADRÃO REUTILIZÁVEL]            [CONFIGURAÇÃO DO CLIENTE]
 antigo VHM-P                    antigo VHM-C
 |                               |
 + Processo versionado           + Objetivos e entregáveis
 + Estados e transições          + Plataformas e formatos
 + Regras e permissões           + Skills e ferramentas
 + Controle de falhas            + Conectores e dependências
 + Registros e métricas          + Metas, prazos e orçamento
 |                               |
 +---------------+---------------+
                 |
                 v
       [INSTÂNCIA CONFIGURADA]
              antigo HPG
                 |
                 v
       [OPERADOR HUMANO — antigo HA]
                 |
       [CONSOLE — antigo HEP]
       Poucos controles operacionais
       A/B/C/D: estados ainda a mapear
                 |
                 v
       [MOTOR DE WORKFLOW]
       Coordena tarefas, estados e retomadas
                 |
                 v
       [AGENTE DE IA]
       Executa tarefas delimitadas
                 |
       [FERRAMENTAS / PLUGINS]
                 |
       [CONECTORES AUTORIZADOS]
                 |
                 v
       [PRODUZIR E DERIVAR] <-----------+
                 |                     |
                 v                     |
       [VALIDAÇÃO E APROVAÇÃO HUMANA]  |
                 |                     |
                 +-- Revisar ----------+
                 |   Retrabalho limitado
                 |
                 +-- Cancelar/limite --> [ENCERRAR]
                 |
                 +-- Aprovar
                       |
                       v
              [AGENDAR E PUBLICAR]
                       |
                       v
              [MONITORAR RESULTADOS]
                       |
                       v
              [ENCERRAR INSTÂNCIA]
                       |
                       v
              [CALCULAR IQO]
                       |
              [ANALISAR DESVIOS]
                       |
              [TESTAR MELHORIA]
                       |
              [VERSIONAR PADRÃO
               OU CONFIGURAÇÃO]
                       |
              [PRÓXIMAS INSTÂNCIAS]
CONTROLES TRANSVERSAIS
Permissões mínimas | Isolamento por cliente | Auditoria
Deduplicação | Retentativas limitadas | Pausa/cancelamento
APLICAÇÃO EDITORIAL
22 tarefas cadastradas
5 fases propostas:
configurar / produzir / derivar / validar / distribuir-monitorar
5 famílias de entregáveis por ciclo:
artigo / vídeo / imagens / quick frameworks / assets CTA
Derivados: 43; total 45 depende de duas saídas identificadas.
Preparação: 14 + 3 = 17 dias.
Publicação: janela de 15 dias; sobreposição a definir.
Tarefas, fases, famílias e peças têm contagens separadas.
QUALIDADE
IQO = 100 × G × mínimo(
  1,
  Q / Q_meta,
  P / P_meta,
  C_limite / C_real
)
Q = aprovadas sem retrabalho / previstas no período
P = aprovadas no prazo / previstas no período
C_real = custo total / entregas aprovadas equivalentes
G = 1: controles críticos atendidos
    0: violação crítica
Sem dados suficientes: não calculável.
Sem entregas aprovadas: ciclo classificado como falha.

C — Contexto. Você desenvolve uma estrutura operacional reutilizável. Cada cliente recebe parâmetros próprios. O humano supervisiona; o motor coordena; o agente executa; os conectores acessam serviços externos.

Q — Questão. Como aceitar personalizações sem tornar a operação cara, lenta ou difícil de manter? A quantidade de variáveis é um sinal investigativo; seu impacto deve aparecer nas entregas, nos custos e nas falhas.

C — Conclusão. O IQO proposto acompanha o pior atendimento relativo às metas. É um indicador próprio, ainda sujeito a validação. Seus componentes permanecem visíveis. FG corresponde ao caminho principal; FB, ao retorno; GPR, à execução monitorada. As antigas equações 1+1=3 e 17/Δ deixam de orientar contagens.

A — Ação. Defina aceite e metas antes do piloto. Registre resultados, identifique o principal desvio, teste uma melhoria e compare ciclos equivalentes. Versione alterações sem mudar retroativamente as metas. Desenvolva o padrão com DMADV e melhore sua operação com DMAIC.  Verifiquei. O framework aparece predominantemente como SCQA — Situation, Complication, Question, Answer, associado ao trabalho de Barbara Minto. “SQCA” também aparece em publicações sobre ele, inclusive alternando com “SCQA” no mesmo artigo. Minha interpretação anterior de CQCA não correspondia ao framework que você pretendia. 

Aplicando a estrutura à sua visão sistêmica:

S — SITUATION / SITUAÇÃO
Você desenvolve um sistema operacional reutilizável.
Cada cliente recebe uma configuração desse sistema.
      PADRÃO DO PROCESSO + CONFIGURAÇÃO DO CLIENTE
                           |
                           v
                  INSTÂNCIA DE EXECUÇÃO
C — COMPLICATION / COMPLICAÇÃO
Novos clientes acrescentam regras, plataformas,
integrações, entregáveis e exceções.
Sem controle, essa personalização pode aumentar:
  - esforço de manutenção;
  - intervenções humanas;
  - retrabalho e falhas;
  - custo e prazo de entrega.
Contar variáveis isoladamente não revela seu impacto.
Q — QUESTION / QUESTÃO
Como personalizar o sistema mantendo qualidade,
produtividade e controle da complexidade?
A — ANSWER / RESPOSTA
Separar o padrão das configurações dos clientes;
executar com supervisão humana; medir resultados;
melhorar o processo com evidências.
[OPERADOR HUMANO]
        |
[CONSOLE OPERACIONAL]
        |
[MOTOR DE WORKFLOW]
Coordena estados, regras e retomadas
        |
[AGENTE DE IA]
Executa tarefas delimitadas
        |
[FERRAMENTAS + CONECTORES]
        |
[PRODUÇÃO E DERIVAÇÃO] <----------------+
        |                              |
[VALIDAÇÃO E APROVAÇÃO]                 |
        |                              |
        +-- Revisar dentro do limite --+
        |
        +-- Cancelar / exceder limite --> [ENCERRAR]
        |
        +-- Aprovar
              |
      [AGENDAR E PUBLICAR]
              |
      [MONITORAR E ENCERRAR]
              |
      [AVALIAR QUALIDADE — IQO]
              |
      [INVESTIGAR DESVIOS]
              |
      [TESTAR E VERSIONAR MELHORIAS]
              |
      [APLICAR NAS PRÓXIMAS INSTÂNCIAS]

A narrativa central fica assim: você investe no padrão reutilizável; configura as particularidades de cada cliente; observa se elas prejudicam as metas; e incorpora melhorias comprovadas às próximas execuções.

O SCQA organiza essa explicação. O BPM organiza a gestão do processo. O workflow coordena sua execução. O IQO proposto acompanha o atendimento às metas:

IQO = 100 × G × mínimo(
  1,
  qualidade / meta de qualidade,
  pontualidade / meta de pontualidade,
  custo-limite / custo-real
)
G = controles críticos atendidos: 1; violação crítica: 0.
Custos comparados por entrega equivalente.
Sem dados suficientes: não calculável.

O número único orienta a investigação; os componentes mostram o que precisa melhorar.