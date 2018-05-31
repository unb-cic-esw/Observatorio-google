# TODO
# Buscar diretamente do heroku os Jsons a partir de duas datas

import pandas as pd
import json
import unicodedata
from text_analyzer import analyze
from sharedcount import sharedcount


# DataFrame contém: hora_busca,link, dominio do link, titulo, 
# posicao na busca, preview e shared count do link e dominio
def get_domain(link):
    left_domain   = link[:link.index('/')+2]
    right_domain = link[link.index('/')+2:]
    right_domain = right_domain[:right_domain.index('/')]
    return left_domain + right_domain
def CreateDataFrame(file_name):    
    # Json contem uma lista de dictionarys(data_coleta->conteudo)
    # Esta funcao cria um DataFrame contendo: data_coleta, link, dominio
    array_dictionaries = []
    file = json.loads(open(file_name).read())    
    for array in file:
        position = 0
        time_search = array["horario"]
        this_data   = array["dados"]
        links       = this_data["Links de Resultados"]        
        titles      = this_data["Titulos de Resultados"]
        previews    = this_data["Previsoes de Resultados"]
        for link,title,preview in zip(links,titles,previews):
            position += 1
        	# Extrai o dominio a partir de string split
            domain = get_domain(link)            
            # Pega o shared count(Facebook) do link
            data = sharedcount(link)
            link_sc = data['Facebook']['share_count']
            # Pega o shared count(Facebook) do dominio
            data = sharedcount(domain)
            domain_sc = data['Facebook']['share_count']
            
            #Cria um dicionario para o array de dicionarios
            this_dictionary = {'time': time_search,'link': link,'domain': domain,
                               'title': title,'position': position,'preview': preview,
                               'link_sc': link_sc, 'domain_sc': domain_sc }
            array_dictionaries.append(this_dictionary)

    # Cria o DataFrame a partir do array de dicionarios
    return pd.DataFrame(array_dictionaries)

def domain_count(data_frame_array):    
    # Concatena todos os data frames do array em um so
    all_dfs = pd.concat( data_frame_array )    
    # Agrupa por dominio e conta as aparicoes de cada link
    count_df = all_dfs.groupby('domain').count()['link']
    print (count_df)

def get_keywords(data_frame_array,num_keywords):
    documents = []
    for df in data_frame_array:
        string = ' '.join(p for p in df['preview'])        
        documents.append(string)
    
    print (analyze( documents, num_keywords ))

# Colocar em all_dfs uma lista de todos os dataframes
# Contenedo os Jsons dentre um range de datas
all_dfs = [CreateDataFrame('in.json'),CreateDataFrame('in2.json')]
#Count itera sobre o array de dataframes apenas para fins de print
count = 1
for dataframe in all_dfs:
    #Busca uma correlação entre o shared count do dominio/link e a posição    
    print("Correlação entre o shared count do link e posição no " +
        str(count) + "º dataframe: ", dataframe['link_sc'].corr(dataframe['position']))
    print("Correlação entre o shared count do dominio e posição no " + 
        str(count) + "º dataframe: ", dataframe['domain_sc'].corr(dataframe['position']))
    print()
    count += 1
print()

domain_count(all_dfs)
print 
get_keywords(all_dfs,10)