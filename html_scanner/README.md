# HTML Scanner

Esse é um módulo que extrai informações de um arquivo HTML.

O arquivo principal é o arquivo html_scanner.py, que é a interface para extrair informações de um arquivo HTML. Basta chamar o método extract_info desse arquivo, passando um html como entrada e a saída é um JSON contendo as informações que foram especificadas dentro de html_scanner.

# Manutenção

Modelamos cada informação relevante como uma classe, e usando classes pra encapsular um conjunto de informações, como se a estrutura do JSON fosse exatamente um diagrama de dependências. 

Por exemplo, se os requisitos de html_scanner são TopStory e GenericResult, teremos um json na seguinte estrutura.
```
{
    PrincipaisNoticias : [
        *retorno dos requisitos da classe TopStory.*
    ],
    Resultado : [
        *retorno dos requisitos da classe GenericResult*
    ]
}
```

O nome PrincipaisNoticias é especificado no arquivo da classe TopStory assim como Resultado é especificado no arquivo da classe GenericResult, e essas classes por si mesmas retornam jsons, então os elementos dos arrays PrincipaisNoticias e Resultado serão JSONs também. 

Então, se quisermos adicionar um novo requisito, ou seja, uma nova informação para ser extraída e vir no JSON resultado, temos que primeiro ver aonde ela se encaixa na hierarquia, então por exemplo, se for uma informação relevante a uma notícia principal, criaríamos uma nova classe para extrair essa informação, e adicionaríamos essa nova classe na lista de requisitos da classe TopStory.

## A ideia
Construímos essa abstração de requisitos, aonde cada informação é um requisito. A invariante é que essa função deve extrair o tipo de dado que representa de forma que a função dados() retorne uma lista dessas informações. Ou seja, TopStoryImage apenas puxa os links para as imagens das principais notícias, de forma que quando chamamos o métodos dados() dessa função obtemos uma lista com os links para todas as imagens de principais notícias.

Essa classe nova pode ser um requisito que puxa informacões atômicas, isto é, uma lista de strings por exemplo, ou um requisito composto, que é uma informação composta de outros requisitos. 

## Tipos de requisito
TopStoryLink é um exemplo de requisito atômico, pois essa funciona de forma que só puxa os links para as principais notícias, e esses dados são atômicos, são strings.

TopStory é um exemplo de requisito composto, pois as informações que compoem uma principal notícia não são atômicos, Pois a principal notícia é composta de TopStoryLink, TopStoryImage e TopStoryPreview, que são requisitos.

### Requisitos Compostos
Para o último caso, a classe CompositeRequirement foi feita para facilitar a criação desse tipo de requisito, baste herdar dessa classe e sobrescrever a função de inicialização para indicar os requisitos. A razão pra isso é que as classes compostas sempre são feitas de vários requisitos, então a implementação herdada de CompositeRequirement implementa isso de maneira genérica. As classes TopStory, Ad, e Result são exemplos. 

### Requisitos atômicos
Para criar requisitos atômicos, devemos constuir uma classe que retorna uma lista de dados atômicos. Requisitos atômicos herdam da classe Requirement, e devem implementar as funções "shandletag", "ehandletag" e "shandledata". 

Os elementos do arquivo HTML são lidos em ordem, e shandletag é a função que define o que aquela classe faz ao encontrar a abertura de uma tag HTML, o nome da tag o atributo "tagin" e opções como class e style vem como uma lista de pares em "attrs".

Análogamente, a função ehandledata define o que aquela classe faz no fechamento de uma tag HTML, e o nome da tag vem em "tagin".  e a função "shandledata" define o comportamento no encontro de um texto que não é abertura nem fechamento de tags HTML. Então em 
```
<p>
texto
</p>
```
O Elemento "p" será encontrado, e vai disparar a função "shandledata" com "p" no argumento "tagin", depois,
elemento "texto" será encontrado, e vai disparar a função "shandledata" com "texto" no argumento "data". Por fim, "/p" vai disparar a função "ehandledata" com "p" como "tagin". Vendo a implementação de algum requisito atômico ajuda a entender melhor.

## Fluxo das operações

A arquitetura de como tudo funciona não é trivial de se compreender, então aqui é uma tentativa de explicar o que está acontecendo com os dados nessa estrutura de classes.

O fluxo todo começa lá no arquivo html_scanner.py, na classe MyParser, que funciona como um requisito composto que representa o escopo mais externo do JSON. Quando chamamos a função run e dentro dela a função feed, mandamos o nosso Parser passar pelos elementos do HTML desencadeando as funções. Essa funcionalidade da função feed é herdada da classe HTMLParser. 

Então, quando estamos querendo cumprir um requisito composto, iteramos sobre todos os subrequisitos propagando as chamadas de "shandletag", "ehandletag" e "shandledata" para os subrequisitos, e isso continua até chegarmos e um requisito atômico, que de fato analisa as tags e usa o padrões de tags em volta da informação desejada para saber quando pegar a informação.

Então, depois que chamamos feed, todas as classes atômicas vão ter já construído sua lista de informações, já que vamos passar por todas as informações em MyParser e isso será propagado por todas as folhas. Após isso,  passamos por cada requisito construindo nosso JSON externo, adicionando a chave igual ao nome do requisito, e o valor igual ao resultado do método dados do requisito e esse métodos dados, vai de maneira recursiva seguindo esse padrão: Sempre que forem os dados de um requisito atômico, é apenas uma lista dessas informações já construída, e quando forem de um requisito composto, é um JSON com os pares chave valor sendo o nome do requisito e os dados provindos daquele requisito.

