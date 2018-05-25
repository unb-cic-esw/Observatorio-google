import pandas as pd
import json
import unicodedata

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

def domain_count():
    # Concatena dois data
    df = CreateDataFrame('in.json')
    all_dfs = pd.concat([df,CreateDataFrame('in2.json')])
    count_df = all_dfs.groupby('domain').count()['link']
    print count_df

df = CreateDataFrame('in2.json')
all_titles = ' '.join(p for p in df['title'])
# Converte de unicode pra string
all_titles = unicodedata.normalize('NFKD', all_titles).encode('ascii','ignore')
print all_titles