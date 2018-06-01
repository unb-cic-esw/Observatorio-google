import json
import os
import urllib.request

def sharedcount(url):
    requestUrl = 'http://api.sharedcount.com/?url=' + url + "&apikey=" + os.environ['SharedCountAPI']
    
    try:
        apiData = urllib.request.urlopen(requestUrl)
        apiJson = json.loads(apiData.read().decode('utf-8'))
    except:
        exit('Error')

    return apiJson

if __name__ == '__main__':
	with open("links.json") as dataFile:
		links = json.load(dataFile)
		for link in links["links"]:
			print(link["link"])
			scRes = sharedcount(link["link"])
			if scRes != 'Error':
				outFile = open(link["name"] + ".json","w+")
				with outFile as f:
					json.dump(scRes, f)
				outFile.close();
