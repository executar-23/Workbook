Parcialmente. Pesquisei as práticas atuais e há uma diferença importante entre o que já é padrão consolidado e o que é um fluxo moderno com agentes de IA.

O que é padrão de mercado

Design Tokens → Design System → Componentes → Páginas é uma arquitetura amplamente estabelecida. O Design Tokens Community Group mantém hoje uma especificação estável para representar e trocar tokens entre ferramentas e código, justamente para manter a linguagem visual consistente. 

O Component-Driven Development também é prática consolidada: construir componentes isoladamente e depois compor telas. O Storybook documenta exatamente esse fluxo — componentes primeiro, telas depois — e é usado por milhares de equipes para desenvolvimento, testes e documentação. 

O que NÃO é um padrão universal

Isto especificamente:

wireframe.txt
→ agente IA
→ React automaticamente

não é um padrão formal da indústria. É um workflow emergente de desenvolvimento assistido por IA.

O equivalente tradicional costuma ser:

Figma / especificação
        ↓
Design System
        ↓
componentes existentes
        ↓
React

A própria Figma está levando essa arquitetura para agentes: o Code Connect conecta componentes visuais diretamente aos componentes reais do repositório e fornece essas referências aos agentes de IA para melhorar a implementação. 

Para o seu projeto, eu melhoraria uma coisa

Em vez de aceitar qualquer .txt livre, criaria um Wireframe Contract oficial:

Wireframe Specification
        ↓
Schema validation
        ↓
Component mapping
        ↓
@platform/design-system
        ↓
React / Next.js
        ↓
Visual + a11y tests

Por exemplo:

page: ArticleDetail
route: /blog/[slug]
layout:
  header: SiteHeader
  main:
    - ArticleHeader
    - ArticleBody
    - InsightCallout
    - NewsletterCard
  aside:
    - TableOfContents
    - RelatedArticles
  footer: SiteFooter

Isso é muito melhor para agentes do que texto totalmente livre.

Portanto, a arquitetura que você está criando está alinhada às práticas profissionais modernas. A inovação específica é transformar o wireframe textual em um contrato machine-readable, permitindo que Claude/Codex gere React de maneira previsível usando apenas seu Design System.

Eu consideraria esse Wireframe → React Contract uma parte formal da arquitetura do projeto, não apenas uma convenção de prompt.