Use este prompt para o agente que receberá o .zip:

Você receberá um arquivo .zip contendo várias imagens de interfaces, telas, fluxos ou wireframes.

Os arquivos de imagem estão nomeados ou numerados, por exemplo:

1.png
2.png
3.png
4.png

Sua tarefa é analisar todas as imagens do ZIP, respeitar a ordem numérica dos arquivos e produzir um único arquivo Markdown (.md), estruturado prioritariamente para ser interpretado por outro agente de IA.

Objetivo

O arquivo Markdown final deve funcionar como uma representação textual completa das imagens, permitindo que outro agente de IA compreenda:

* o contexto geral do produto/interface;
* quais telas existem;
* a ordem e numeração das telas;
* o conteúdo visual de cada imagem;
* a estrutura/layout;
* os componentes presentes;
* textos, labels e informações visíveis;
* relações entre elementos;
* possíveis interações;
* navegação entre telas;
* estados da interface;
* hierarquia visual;
* wireframe textual completo de cada imagem.

Não produza apenas uma descrição visual superficial.

O resultado deve permitir que outro agente reconstrua a interface com o máximo de fidelidade possível mesmo sem ter acesso às imagens originais.

⸻

Processo obrigatório

1. Extraia e identifique todas as imagens do ZIP.
2. Ordene os arquivos numericamente pelo nome.
3. Analise individualmente cada imagem.
4. Identifique padrões compartilhados entre as telas.
5. Identifique componentes reutilizados.
6. Identifique possíveis relações de navegação entre telas.
7. Gere um único arquivo .md.
8. Não gere um arquivo separado para cada imagem.
9. Não ignore imagens duplicadas ou aparentemente semelhantes; documente-as e explique as diferenças.
10. Não invente informações que não possam ser observadas ou inferidas razoavelmente.

Quando alguma informação for incerta, utilize explicitamente:

[INCERTO]

Quando estiver fazendo uma inferência baseada no conjunto das telas, utilize:

[INFERIDO]

⸻

Estrutura obrigatória do Markdown

O arquivo deve seguir exatamente esta organização geral:

Interface Analysis

1. Contexto Geral

Descreva o que o conjunto de imagens aparenta representar.

Inclua:

* tipo de aplicação;
* objetivo provável;
* domínio do produto;
* perfil provável de usuário;
* estrutura geral da experiência;
* padrões visuais recorrentes;
* dispositivos/formato aparente;
* quantidade total de imagens analisadas.

2. Índice das Telas

Crie uma tabela:

ID	Arquivo	Nome inferido da tela	Descrição curta
001	1.png	…	…
002	2.png	…	…

Use IDs normalizados com três dígitos:

001, 002, 003 etc.

Preserve também o nome original do arquivo.

3. Arquitetura Geral da Interface

Descreva os elementos recorrentes encontrados no conjunto inteiro:

3.1 Navegação

3.2 Header

3.3 Sidebar

3.4 Conteúdo principal

3.5 Modais e overlays

3.6 Formulários

3.7 Botões e ações

3.8 Tipografia e hierarquia visual

3.9 Componentes reutilizáveis

3.10 Estados da interface

Inclua apenas as seções aplicáveis.

4. Fluxo entre Telas

Quando for possível identificar relações entre imagens, represente o fluxo.

Exemplo:

[001 Login]
    |
    +--> ação: Entrar
            |
            v
[002 Dashboard]
    |
    +--> ação: Novo projeto
            |
            v
[003 Criar Projeto]

Não invente transições.

Utilize [INFERIDO] quando a relação não estiver explicitamente demonstrada.

⸻

5. Telas

Crie uma seção para cada imagem, sem exceção.

Formato obrigatório:

Tela 001 — Nome da Tela

Arquivo: 1.png

ID: 001

Objetivo da tela

Explique a função aparente da tela.

Contexto

Explique onde essa tela parece estar dentro da aplicação e sua relação com outras telas.

Estrutura visual

Descreva a tela de cima para baixo e da esquerda para a direita.

Informe:

* regiões;
* containers;
* colunas;
* barras;
* cards;
* divisores;
* alinhamentos;
* espaçamentos aparentes;
* hierarquia.

Componentes identificados

Liste cada componente relevante.

Para cada componente, informe:

* tipo;
* posição;
* conteúdo;
* estado;
* interação aparente;
* relação com outros componentes.

Conteúdo textual

Transcreva os textos visíveis sempre que forem legíveis.

Não corrija ou altere o conteúdo original silenciosamente.

Se algum texto não puder ser identificado:

[TEXTO ILEGÍVEL]

Elementos interativos

Documente:

* botões;
* links;
* campos;
* selects;
* checkboxes;
* tabs;
* menus;
* ícones clicáveis;
* paginação;
* controles;
* ações disponíveis.

Quando uma ação não puder ser determinada:

Ação: [INCERTO]

Estado da interface

Exemplos:

* default;
* loading;
* empty;
* error;
* success;
* modal aberto;
* formulário preenchido;
* dropdown aberto;
* item selecionado;
* hover aparente;
* confirmação.

Wireframe textual

Crie um wireframe ASCII detalhado da imagem.

Exemplo:

┌──────────────────────────────────────────────────────────────┐
│ Logo                     Busca                 Perfil        │
├───────────────┬──────────────────────────────────────────────┤
│               │ Dashboard                                    │
│ Dashboard     │                                              │
│ Projetos      │ ┌────────────┐ ┌────────────┐               │
│ Clientes      │ │ Card 01    │ │ Card 02    │               │
│ Configuração  │ └────────────┘ └────────────┘               │
│               │                                              │
│               │ Projetos recentes                            │
│               │ ┌──────────────────────────────────────────┐ │
│               │ │ Nome        Status        Ações          │ │
│               │ ├──────────────────────────────────────────┤ │
│               │ │ Projeto A   Ativo         ...            │ │
│               │ └──────────────────────────────────────────┘ │
└───────────────┴──────────────────────────────────────────────┘

O wireframe deve representar:

* posição relativa;
* agrupamentos;
* hierarquia;
* containers;
* textos;
* componentes;
* botões;
* campos;
* navegação;
* overlays;
* elementos relevantes.

Não simplifique excessivamente.

Relações com outras telas

Exemplo:

001
 ├── botão "Entrar" -> 002 [INFERIDO]
 └── link "Esqueci minha senha" -> 005 [INFERIDO]

Observações

Registre detalhes que possam ser importantes para reconstrução da interface.

⸻

Repita esta estrutura para:

Tela 002, Tela 003, Tela 004…

até que todas as imagens tenham sido documentadas.

⸻

6. Componentes Compartilhados

Depois das telas individuais, consolide os componentes reutilizados.

Formato:

Component: Sidebar

Presente em: 002, 003, 004, 008

Estrutura

Conteúdo

Estados observados

Variações

Comportamento inferido

Repita para headers, cards, tabelas, formulários, modais, menus, botões e outros componentes relevantes.

⸻

7. Mapa de Navegação

Produza uma representação consolidada do sistema.

Aplicação
├── Autenticação
│   ├── 001 Login
│   └── 002 Recuperação de senha
│
├── Área principal
│   ├── 003 Dashboard
│   ├── 004 Projetos
│   └── 005 Detalhes do projeto
│
└── Configurações
    └── 006 Configurações

Utilize somente relações observadas ou marque inferências.

⸻

8. Inventário Final

Crie um resumo estruturado contendo:

* número total de imagens;
* número total de telas distintas;
* componentes globais;
* componentes exclusivos;
* modais encontrados;
* formulários encontrados;
* tabelas encontradas;
* estados diferentes encontrados;
* possíveis fluxos;
* telas semelhantes;
* telas que parecem representar variações de estado.

⸻

Regras de precisão

Priorize fidelidade às imagens sobre interpretações criativas.

Não:

* invente telas;
* invente textos;
* invente funcionalidades;
* omita imagens;
* agrupe imagens diferentes sem documentá-las individualmente;
* trate inferências como fatos;
* substitua o wireframe por uma descrição genérica.

Se duas imagens forem praticamente iguais, registre ambas e explique exatamente o que mudou.

Exemplo:

Tela 014 é semelhante à Tela 013, porém apresenta o modal de confirmação aberto.

Formato de saída

Entregue somente um arquivo Markdown.

Nome preferencial:

interface-analysis.md

O documento deve utilizar Markdown simples e sem dependências externas.

Priorize uma estrutura semântica e previsível para facilitar parsing por LLMs/agentes de IA.

Utilize:

* headings consistentes;
* IDs consistentes;
* tabelas Markdown;
* blocos de código para wireframes;
* relações explícitas entre IDs;
* textos objetivos;
* marcações [INCERTO] e [INFERIDO].

O documento final deve ser autocontido e compreensível sem acesso às imagens originais.

Esse formato é especialmente útil se o próximo agente for responsável por transformar as imagens em código, pois separa contexto global, telas, componentes, estados e relações de navegação.