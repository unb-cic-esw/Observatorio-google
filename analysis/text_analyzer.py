from __future__ import division
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import math
import operator

def filter_words(document):
    # Retira StopWords(artigos, adverbios ... dos textos)
    wordsFiltered = []
    stopWords_pt = set(stopwords.words('portuguese'))
    stopWords_eng = set(stopwords.words('english'))
    tokens = word_tokenize(document)
    for w in tokens:
        if (w not in stopWords_pt) and (w not in stopWords_eng) and (len(w) > 1) and (w != '...') and (w != '\'s'):
            wordsFiltered.append(w)
    
    return wordsFiltered
def word_frequency(document):
    # Num vezes aparece/Total palavras do doc
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

def analyze(documents,num_palavras_chaves):    
    for i,val in enumerate(documents):
        # Fitra as palavras de todos os documentos
        documents[i] = filter_words(documents[i].lower())

    # Cria um dictionary contendo todos os termos e respectivos idfs
    idf = {}
    # Cria uma lista contendo todas as frequencias de termos
    word_frequency_list = []
    for doc in documents:    
        tf = word_frequency(doc)    
        word_frequency_list.append(tf)
        # Usa o tf para calcular o idf      
        idf = dict(idf, ** inverse_word_frequency(documents,tf))       

    # Cria uma lista de relevancia 
    relevance_list = {}    
    for term_index,val in enumerate(word_frequency_list):
        term_frequency = word_frequency_list[term_index]
        for i in term_frequency:
            relevance_list[i] = term_frequency[i] * idf[i]

    # Cria uma lista de frequencia
    top_frequency = Counter(documents[0])
    for i in range(1,len(documents)):
        y = Counter(documents[i])
        top_frequency = { k: top_frequency.get(k,0) + y.get(k,0) for k in set(top_frequency) }
        
    # Ordena de forma descendente as listas de 'top'
    top_relevant = sorted(relevance_list.items(), key=operator.itemgetter(1))
    top_relevant = top_relevant[::-1]

    top_frequency = sorted(top_frequency.items(), key=operator.itemgetter(1))
    top_frequency = top_frequency[::-1]
    # Mostra os 10 itens mais relevantes e frequentes daquela pesquisa
    top_relevant = [x[0] for x in top_relevant[:num_palavras_chaves]]
    top_frequency = [str(x[0]) + '(' + str(x[1]) + ')' for x in top_frequency[:num_palavras_chaves]]
    # Retorna uma string contendo: 10 palavras mais relevantes e as 10 mais frequentes
    return (str(num_palavras_chaves) + " palavras mais relevantes: " + ', '.join(top_relevant) + '\n'
            )+ (str(num_palavras_chaves) + " palavras mais frequentes: " + ', '.join(top_frequency))
    
