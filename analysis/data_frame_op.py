import json
import sys
import os
import urllib.request
import pandas as pd
from text_analyzer import analyze

# Modulo definido para operacoes com data frames
# Como criacao e analises.

def shared_count(url):
    # Dado um url, exporta seu shared count
    request_url = ('http://api.sharedcount.com/?url=' + url +
                   "&apikey=" + os.environ['SharedCountAPI'])

    try:
        api_data = urllib.request.urlopen(request_url)
        api_json = json.loads(api_data.read().decode('utf-8'))
    except:
        exit('Error')

    return api_json

# DataFrame contem: hora_busca,link, dominio do link, titulo,
# posicao na busca, preview e shared count do link e dominio
def get_domain(link):
    left_domain = link[:link.index('/')+2]
    right_domain = link[link.index('/')+2:]
    right_domain = right_domain[:right_domain.index('/')]
    return left_domain + right_domain

def get_json(actor):
    # Pega os dados do heroku
    print('Fetching ' + actor + ' data...')
    request_url = "https://observatorio-google.herokuapp.com/api/pesquisas/ator/"    
    with urllib.request.urlopen(request_url + actor) as url:
        data = json.loads(url.read().decode())
        print('Done!')
        return data

def get_json_info(json_data, name):
    result = []
    for atribute in json_data:
        result.append(atribute[name])
    return result

def create_data_frame(fetched_json):
    # Json contem uma lista de dictionarys(data_coleta->conteudo)
    # Esta funcao cria um DataFrame contendo: data_coleta, link, dominio
    print('Creating Dataframe...')
    array_dictionaries = []
    i=0
    for array in fetched_json:
        position = 0
        i+=1
        print('============' + str(i))        
        try:
            time_search = array['dados']['data']
            this_data = array['dados']['Resultado']
            links = get_json_info(this_data, 'linkResultados')
            titles = get_json_info(this_data, 'tituloResultados')
            previews = get_json_info(this_data, 'previsaoResultados')
        except:
            print('nop')
            continue
        for link, title, preview in zip(links, titles, previews):
            position += 1
            # Extrai o dominio a partir de string split
            domain = get_domain(link)
            # Pega o shared count(Facebook) do link
            data = shared_count(link)
            link_sc = data['Facebook']['share_count']
            # Pega o shared count(Facebook) do dominio
            data = shared_count(domain)
            domain_sc = data['Facebook']['share_count']
            #Cria um dicionario para o array de dicionarios
            this_dictionary = {'time': time_search, 'link': link, 'domain': domain,
                               'title': title, 'position': position, 'preview': preview,
                               'link_sc': link_sc, 'domain_sc': domain_sc}
            array_dictionaries.append(this_dictionary)

    # Cria o DataFrame a partir do array de dicionarios
    print('Created!')
    return pd.DataFrame(array_dictionaries)

def domain_count(data_frame_array):
    # Concatena todos os data frames do array em um so
    all_dfs = pd.concat(data_frame_array)
    # Agrupa por dominio e conta as aparicoes de cada link
    count_df = all_dfs.groupby('domain').count()['link']
    print(count_df)
    return count_df

def get_keywords(data_frame_array, num_keywords):

    documents = []
    for data_frame in data_frame_array:
        string = ' '.join(p for p in data_frame['preview'])
        documents.append(string)

    print(analyze(documents, num_keywords))

def main(arg):
    # Colocar em all_dfs uma lista de todos os dataframes
    # Contendo os Json's desejados
    fetched_json = get_json(arg)
    all_dfs = [create_data_frame(fetched_json)]
    # Count itera sobre o array de dataframes apenas para fins de print
    count = 1
    for dataframe in all_dfs:
        # Busca uma correlação entre o shared count do dominio/link e a posição
        print("Correlação entre o shared count do link e posição no " +
              str(count) + "º dataframe: ", dataframe['link_sc'].corr(dataframe['position']))
        print("Correlação entre o shared count do dominio e posição no " +
              str(count) + "º dataframe: ", dataframe['domain_sc'].corr(dataframe['position']))
        print()
        count += 1
    print()

    domain_count(all_dfs)
    print()
    get_keywords(all_dfs, 10)

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("Por favor mande um ator como parâmetro")
    else:       
        # Prepara os argumentos para enviar a um url 
        l = sys.argv
        l.pop(0)
        string = '%20'.join(l)        
        main(string)
