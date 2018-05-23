import pandas as pd
import json

def CreateDataFrame(file_name):    
    # Json contem uma lista de dictionarys(data_coleta->conteudo)
    # Esta funcao cria um DataFrame contendo: data_coleta, link, dominio
    array_dictionaries = []
    file = json.loads(open(file_name).read())
    for array in file:
        time_search = array["time"]
        this_data   = array["data"]
        links       = this_data["link Resultado"]        
        for link in links:
        	# Extrai o dominio a partir de string split
            domain = link[link.index('.')+1:]
            domain = domain[:domain.index('.')]
            #Cria um dicionario para o array de dicionarios
            this_dictionary = {'time': time_search,'link': link,'domain': domain}
            array_dictionaries.append(this_dictionary)

    # Cria o DataFrame a partir do array de dicionarios
    df = pd.DataFrame(array_dictionaries)
    # Seleciona primeiras 5 linhas
    print df.iloc[0:5,:]
        
CreateDataFrame("in.json")