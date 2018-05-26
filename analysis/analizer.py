# TODO
# Adicionar posicao no dataframe(e shared count)
# Extender o get keywords para possivelmente o texto do html 
# (mais interessante por conta do cálculo da relevância)
# Buscar diretamente do heroku os Jsons a partir de duas datas

import pandas as pd
import json
import unicodedata
from text_analyzer import analyze

def CreateDataFrame(file_name):    
    # Json contem uma lista de dictionarys(data_coleta->conteudo)
    # Esta funcao cria um DataFrame contendo: data_coleta, link, dominio
    array_dictionaries = []
    file = json.loads(open(file_name).read())
    
    for array in file:
        time_search = array["horario"]
        this_data   = array["dados"]
        links       = this_data["Links de Resultados"]        
        titles      = this_data["Titulos de Resultados"]
        for link,title in zip(links,titles):
        	# Extrai o dominio a partir de string split
            domain = link[link.index('/')+2:]
            domain = domain[:domain.index('/')]
            
            #Cria um dicionario para o array de dicionarios
            this_dictionary = {'time': time_search,'link': link,'domain': domain,'title': title}
            array_dictionaries.append(this_dictionary)

    # Cria o DataFrame a partir do array de dicionarios
    return pd.DataFrame(array_dictionaries)

def domain_count(data_frame_array):    
    # Concatena todos os data frames do array em um so
    all_dfs = pd.concat( data_frame_array )    
    # Agrupa por dominio e conta as aparicoes de cada link
    count_df = all_dfs.groupby('domain').count()['link']
    print count_df

def get_keywords(data_frame_array,num_keywords):
    documents = []
    for df in data_frame_array:
        string = ' '.join(p for p in df['title'])
        # Converte de unicode pra string
        string = unicodedata.normalize('NFKD', string).encode('ascii','ignore')
        documents.append(string)
    
    analyze( documents, num_keywords )

all_dfs = [CreateDataFrame('in.json'),CreateDataFrame('in2.json')]
domain_count(all_dfs)
print 
get_keywords(all_dfs,10)