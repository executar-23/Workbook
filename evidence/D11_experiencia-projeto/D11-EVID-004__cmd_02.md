/web-artifacts-builder   Desenvolva um artefato funcional reproduzindo a página completa apresentada na imagem de referência.

OBJETIVO
Reconstruir toda a landing page, do topo até o rodapé, como uma página única e rolável.

REQUISITOS

1. Analise a imagem completa de cima para baixo.
2. Identifique todas as seções visíveis.
3. Reproduza todas as seções na mesma ordem da referência.
4. Não implemente somente o Hero ou a área inicialmente visível.
5. A altura da página deve ser determinada pelo conteúdo completo.
6. O resultado deve permitir scroll vertical por toda a página.
7. Preserve:
   - hierarquia visual;
   - proporções;
   - espaçamentos;
   - alinhamentos;
   - grids;
   - cards;
   - botões;
   - tipografia;
   - bordas;
   - fundos;
   - imagens;
   - containers.

8. Desenvolva também a versão responsiva para mobile.

ESTRUTURA ESPERADA

A página parece conter aproximadamente:

01. Header / navegação
02. Hero principal
03. Barra de benefícios/recursos
04. Grid de propriedades/cards
05. Seção "User guide for first timer"
06. Seção de apresentação/conteúdo
07. Bloco de estatísticas
08. Seção institucional
09. Grid/listagem adicional
10. Seção de conteúdos/artigos
11. Rodapé

Analise a referência para determinar a estrutura exata.

FIDELIDADE VISUAL

Use a imagem fornecida como fonte principal de verdade.

Não simplifique seções.
Não remova elementos por parecerem repetitivos.
Não transforme toda a página em uma única imagem.
Os elementos devem ser componentes reais da interface.

Se algum texto não estiver legível, utilize conteúdo provisório semanticamente equivalente e marque no código como conteúdo aproximado.

RESPONSIVIDADE

Desktop:
- reproduzir a composição principal da imagem.

Mobile:
- reorganizar grids em uma coluna;
- adaptar navegação;
- manter hierarquia;
- preservar todas as seções.

ENTREGA

Crie um único artefato executável contendo a página completa.

O artefato deve abrir diretamente na página implementada e permitir navegar verticalmente desde o Header até o Footer.

Antes de finalizar, confira se TODAS as regiões existentes na imagem de referência possuem uma representação correspondente no artefato.03 + 05 → 06 + 07 → 10-group + 10-mini → 02 → 04 → 08 → 11
Interpretação:
● 03 + 05: captura comercial/atenção;
● 06 + 07: seleção de área + movimento;
● 10: variantes de cards;
● 02: card/detail aberto;
● 04: onboarding/instruções;
● 08: composição full-screen da Store;
● 11: composição comercial final.
Planeje o fluxo por estados do usuário; não por filename.
Funcionalidades da rota
A Store deve contemplar, quando suportado pelos contratos:
● hero/comercial;
● Search;
● Filter;
● Sort;
● Collections;
● seleção por área;
● cards multiformato;
● card/detail;
● Start;
● Download quando aplicável;
● onboarding;
● Learn/related content;
● loading/empty/error/retry;
● analytics;
● acessibilidade;
● responsive;
● reduced motion.
Start e Download são semanticamente diferentes.Wireframes
→ estrutura
→ hierarquia
→ interação
→ motion

Design System EXECUTAR
→ cores
→ fontes
→ spacing
→ radius
→ shadows
→ iconografia
→ identidade final 03 + 05
↓
06 + 07
↓
10-group + 10-mini
↓
02
↓
04
↓
08
↓
11 03 + 05
COMERCIAL / CAPTA ATENÇÃO
        ↓
06 + 07
SELEÇÃO DE ÁREA / MOVIMENTO
        ↓
10-group + 10-mini
FAMÍLIA DE CARDS + VARIAÇÕES + MOTION
        ↓
02
CARD ABERTO / DETALHE
        ↓
04
ONBOARDING / INSTRUÇÕES / COPY
        ↓
08
ARQUITETURA FULL-SCREEN DA OFICINA
        ↓
11
VIEW COMERCIAL FINAL COMPLETA    Use este prompt para o Cloud:
# Tarefa — Montar coleção inicial da Solution Store

Você tem acesso às skills disponíveis no próprio ambiente/sistema em que está executando. Use essas skills reais como fonte primária para construir uma coleção inicial da EXECUTAR Solution Store.

Não invente skills, comandos, capacidades ou metadados. Antes de produzir a interface:

1. descubra/lista as skills acessíveis no ambiente;
2. leia os arquivos `SKILL.md`, manifests, schemas e metadados relacionados;
3. identifique as 10 skills mais adequadas para formar uma coleção demonstrativa;
4. normalize os dados para o contrato da Solution Store.

## Objetivo

Produzir uma implementação completa contendo:

- coleção de **10 Solution Cards**;
- páginas de detalhe;
- todas as rotas necessárias;
- onboarding de cada solução;
- copy completa;
- estados de interface;
- CTAs;
- dados estruturados para renderização.

## Para cada um dos 10 cards

Preencher com dados reais da skill:

```yaml
solution:
  id:
  name:
  version:
  status:
  capability_type:
  category:
  area:
  tags:
  headline:
  short_description:
  problem_summary:
  outcome:
  audience:
  deliverables:
  time_to_value:
  slash_commands:
  dependencies:
  cta_primary:
  cta_secondary:
Copy obrigatória
Cada solução deve possuir:

* eyebrow;
* título;
* headline;
* descrição curta;
* descrição completa;
* problema;
* para quem é;
* resultado esperado;
* entregáveis;
* como funciona;
* requisitos;
* comandos disponíveis;
* exemplo de uso;
* CTA Start;
* CTA Download, quando aplicável;
* textos do onboarding.

Rotas
Implementar pelo menos:
/solutions
/solutions/[slug]

/solutions/[slug]/start
/solutions/[slug]/start/intro
/solutions/[slug]/start/context
/solutions/[slug]/start/setup
/solutions/[slug]/start/example
/solutions/[slug]/start/execute

/collections
/collections/executar

/categories/[slug]
/search
Onboarding
Cada Start deve abrir:
01 — O que é
02 — O que você precisa
03 — Como funciona
04 — Exemplo
05 — Executar
A etapa final deve apresentar a ação/comando real da skill.
Coleção
Criar uma seção:
EXECUTAR — Operational Skills
com exatamente 10 cards derivados das skills reais encontradas.
A coleção deve demonstrar diversidade entre:

* copilotos;
* workflows;
* generators;
* especialistas;
* ferramentas;
* orquestradores;

somente quando essas categorias existirem de fato no ambiente.
Regra de arquitetura
A skill é a fonte canônica.
SKILL.md / metadata
        ↓
normalized solution object
        ↓
Solution Store
   ├── Card
   ├── Detail
   ├── Onboarding
   ├── Search
   └── Execution
Não copie manualmente informação divergente entre telas.
Crie um objeto estruturado por solução e faça as interfaces consumirem esse objeto.
Resultado esperado
Entregue a experiência completa e navegável, não apenas wireframes ou placeholders.
Antes de finalizar, valide:

* 10 cards existentes;
* nenhuma skill fictícia;
* todas as rotas funcionando;
* todas as copies preenchidas;
* nenhum Lorem Ipsum;
* Start conectado ao onboarding;
* comandos coerentes com a skill original;
* componentes reutilizáveis;
* responsividade desktop/mobile.