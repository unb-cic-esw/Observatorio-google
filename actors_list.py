import urllib.request
import sys

def retrieve_actors():
    url = "https://gist.githubusercontent.com/maxstabile/739980036872608ca2633331aca9166b/raw/3fb21ca421aa2f958c0e02d83d7e71b5caf2ebbe/actors.txt"
    actors_list = []
    try:
        for data in urllib.request.urlopen(url):
            string = data.decode("utf-8").rstrip()
            actors_list.append(string)
        print("Pesquisando os atores: " + ', '.join(actors_list))
        return actors_list
        
    except :
        print('Não foi possível abrir o arquivo do gist')
        return None

if __name__ == "__main__":
    retrieve_actors()