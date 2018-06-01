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
