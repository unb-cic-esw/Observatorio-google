from __future__ import division
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import math
import operator

data1 = "Lula tera pre-candidatura lancada no dia 9 de junho e PT aposta que ... Sob gritos de apoio e protestos, Gleisi le carta de Lula a prefeitos ... Lula - Pagina inicial | Facebook Lula | Lula PT lancara candidatura de Lula em ato no dia 9 de junho, em Belo ... Caso Lula consiga ser candidato e venca disputa presidencial, tera de ... Lula - ISTOE Independente Ministro do STF autoriza visita de deputados ao ex-presidente Lula ... Reitor de Aparecida se desculpa apos pedir que 'Nossa Senhora ..."
data2 = "Luiz Inacio Lula da Silva - Wikipedia Luiz Inacio Lula da Silva Fast Facts - CNN - CNN.com Luiz Inacio Lula da Silva | World | the Guardian Million-Dollar Accusations Fly Against Brazil's Jailed Ex-President Lula Luiz Inacio Lula da Silva - the New York Times Brazil's Lula: 'Only death will take me off streets' - BBC News - BBC.com Lula Cafe Perry Anderson  Lula's Brazil  LRB 31 March 2011 Lula's legacy | The Economist Lula May Be in Jail, but Brazil's Occupy Movement Won't Let Hope Die ... Profile: Luiz Inacio Lula da Silva | Brazil News | Al Jazeera"
documents = [data1,data2]

def filter_words(document):
    wordsFiltered = []
    stopWords = set(stopwords.words('portuguese'))
    stopWordse = set(stopwords.words('english'))
    tokens = word_tokenize(document)
    for w in tokens:
        if (w not in stopWords) and (w not in stopWordse) and (len(w) > 1) and (w != '...') and (w != '\'s'):
            wordsFiltered.append(w)
    
    return wordsFiltered
def word_frequency(document):
    word_freq = Counter(document)
    for i in word_freq:
        word_freq[i] = word_freq[i]/len(word_freq)
    return word_freq    

def num_appearences_docs(documents,term):
    # Conta em quantos documentos um termo esta 
    count = 0
    for i in documents:
        if term in i:
            count += 1
    return count            

def inverse_word_frequency(documents,term_frequency):
    idf = {}
    for term in term_frequency:
        calc = math.log(len(documents)/num_appearences_docs(documents,term))
        idf[term] = calc
    return idf

for i,val in enumerate(documents):
    documents[i] = filter_words(documents[i])

idf = {}
for doc in documents:    
    tf = word_frequency(doc)      
    idf = dict(idf, ** inverse_word_frequency(documents,tf))       

first_tf = word_frequency(documents[0])
second_tf = word_frequency(documents[1])
relevance_list = {}
for i in first_tf:
    relevance_list[i] = first_tf[i]*idf[i]

for i in second_tf:
    relevance_list[i] = second_tf[i]*idf[i]

sorted_dict = sorted(relevance_list.items(), key=operator.itemgetter(1))
sorted_dict = sorted_dict[::-1]
for i in  sorted_dict[:10]:
    print i
    