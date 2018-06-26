# Módulo de análise
Esse módulo foi desenvolvido para facilitar a compreensão dos dados extraídos pelos outros.

Existe um fluxo grande de informações geradas e, para facilitar a 
visualização do usuário, é importante que exista um processamento destes.

## Instalação do módulo
Primeiramente é necessário baixar as dependências da biblioteca *NLTK*.  
Para tanto, confira se realmente está na pasta *analysis* e basta digitar o seguinte comando no terminal e elas serão baixadas automaticamente:

```
python setup.py
```

Além disso adicione sua chave do *shared count* com:
```
export SharedCountAPI=SUA_CHAVE_AQUI
```

Caso não tenha uma, basta acessar este [link](https://www.sharedcount.com/) para criar uma paga ou de graça.

Obs.: Garanta o seu *virtual enviroment* esteja configurado com as dependências como explica o tutorial de [instalação.](https://github.com/unb-cic-esw/Observatorio-google/wiki/Realizando-coleta-dos-resultados-de-pesquisas-no-Google)

## Execução

### Execução dos testes
Para ter certeza que todas as ferramentas foram instaladas execute os testes.
Assim, garanta que esteja na pasta *analysis/tests/* e basta digitar:

```
pytest
```

E, caso tudo tenha dado certo, a seguinte mensagem deve aparecer:

```
collected 9 items                                                                

test_analyzer.py ...... [ 66%]
test_data_frames.py ... [100%]

================ 9 passed in 11.15 seconds ================
```
### Execução do módulo
Para executar a análise sobre um ator é necessário que seja passado o nome de um como parâmetro, por
exemplo
```
python data_frame_op.py ciro 2018
```

caso nenhum seja suprido, a mensagem de erro deve aparecer como no seguinte exemplo:

```
python data_frame_op.py 
Por favor mande um ator como parâmetro
```

## Arquitetura
Para realizar o que foi especificado esse módulo utiliza dois arquivos: *data_frame_op.py* e *text_analyzer.py*. Como seu nome sugere, primeiro é encarregado de criar os *Data Frames* (unidades de dados básicas do *Data Science*) e modelá-los conforme necessário. Já o segundo se encarrega de processamento textual.

### Data Frames
Agora, será melhor explicado o funcionamento do arquivo *data_frame_op.py*.
Cada **Dataframe** corresponde a pesquisa feita no **Google**. 
Este, por sua vez, contém os seguintes atributos: 
- Tempo em que foi feita a pesquisa;
- *Links*;
- Dominínios correspondentes aos *Links*;
- Título da notícia;
- Posição da mesma na pesquisa (se foi a primeira, segunda, etc);
- *Preview* da notícia;
- *Shared Count* do domínio e do *link*;

*Obs.: Shared Count é uma ferramenta que disponibiliza quantas vezes um link foi compartilhado em redes sociais.*

Para popular os **Dataframe's** devem ser supridos um ou mais *Json's*. Se este módulo for executado como fluxo principal (como programa *main*) esses dados serão obtidos do banco de dados desenvolidos no projeto.
O banco pode ser acessado [aqui](Observatorio-google.herokuapp.com).
Neste arquivo, além de criação de **Dataframe's**, é feita também a contagem de quantas vezes um domínio apareceu em uma ou mais pesquisas.

### Processamento textual
Nesta seção será explanado de modo mais minuncioso o funcionamento do arquivo *text_analyzer.py*. 
A ele, são passados os *Preview's* (correspondentes à pré-visualização de uma notícia).  
Foi escolhida esta seção do *Data Frame* pois é a que possui mais palavras. Essa característica é 
importante para o processamento, pois, quanto maior for o documento analisado, maior será o grau de 
comparação e, assim, a análise de relevância será de maior valor.  
Este arquivo se encarrega de gerar dois resultados: Frequência e relevância das palavras dadas como 
*input*. Para contagem de palavras, usa-se o *Counter*, estrutura do **Python** para contar frêquencias de 
uma *string* em um *array de strings*. Para análise de relevância, foi implementado o algoritmo [*tf-idf*](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).  
Além disso, é importante frisar que, para o processamento ser mais efetivo, é necessário ignorar algumas 
palavras como artigos, advérbios, etc. Para tanto, é usada a biblioteca [*nltk*](https://www.nltk.org/) 
no método *filter-words*, que, como o nome indica, filtra tais palavras.