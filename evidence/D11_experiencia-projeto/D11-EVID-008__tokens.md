Tokens visuais extraídos das quatro imagens

Precisão: as imagens são capturas rasterizadas. Cores, dimensões e fontes abaixo são aproximações visuais, não valores exportados de um arquivo de design. As quatro imagens também não comprovam uma marca única.

Grupo	Token proposto	Valor aproximado e uso
Superfícies	color.canvas	#F5F6F7 — fundo cinza quase branco
Superfícies	color.surface	#FFFFFF — cards e diálogo
Texto	color.ink	#1B2228 — títulos e valores
Texto	color.muted	#657078 — descrições e metadados
Divisórias	color.line	#DCE3E7 — bordas e separadores
Ação	color.brand	#218FE4 — botão de compartilhar e ações principais
Estado	color.success / color.danger	#277D67 / #B24343 — sucesso e erro propostos
Gradientes	lime, orange, mint, violet	#BBD568, #FF9F4D, #78D8AC, #A66BC6 — faixas dos planos

Por imagem

* IMG_3435.JPG — card de tarefa: faixa superior azul vivo; card branco com cantos bem arredondados; placa externa cinza claro e sombras suaves em camadas. Título preto dominante, descrição cinza em até três linhas, avatares sobrepostos, status em cápsula cinza e rodapé com ícones, contagens e data. A borda tracejada interna é um recurso decorativo da referência.
* IMG_3437.JPG — dois planos: cards brancos altos, borda fina com leve cor, cantos arredondados e bastante espaço vazio. Preço grande e preto, /month pequeno, benefícios com marca de verificação multicolorida. O plano “Popular” usa selo escuro. O CTA ocupa toda a base: limão → laranja no primeiro card; ciano → menta no segundo.
* IMG_3438.JPG — três planos: painel branco central sobre fundo cinza quente. Cards estreitos com sombra difusa; o plano do meio ganha contorno rosa/violeta e botão azul/violeta. Títulos, preços e listas formam uma hierarquia compacta. Serve como referência de comparação e destaque, não para copiar os valores comerciais.
* IMG_3428.PNG — compartilhamento: diálogo branco sobre interface escurecida; abas segmentadas cinza, campo de busca cinza claro, linhas de pessoas e permissões, botão azul de largura total e aviso informativo azul pálido. “Done” funciona como ação de fechar.

Escala proposta para implementação

Espaçamentos 4 / 8 / 16 / 24 / 32 / 48 px; raios 8 / 12 / 20 px; corpo 14 px, título 28 px, destaque 40 px; fonte Inter com fallback de sistema. Quebras propostas: mobile abaixo de 640 px, tablet até 959 px, desktop a partir de 960 px. Movimento curto de 120–200 ms, respeitando preferência por movimento reduzido.

Os valores implementáveis estão em tokens.json e tokens.css dentro do pacote entregue⁠￼.