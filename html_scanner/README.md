# HTML Scanner

Esse é um módulo que extrai informações de um arquivo HTML.

O arquivo principal é o arquivo html_scanner.py, que é a interface para extrair informações de um arquivo HTML. Basta chamar o método extract_info desse arquivo, passando um html como entrada e a saída é um JSON contendo as informações que foram especificadas dentro de html_scanner.

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

O nome PrincipaisNoticias é especificado no arquivo da classe TopStory assim como Resultado é especificado no arquivo da classe GenericResult, e essas classes por si mesmas retornam jsons, 