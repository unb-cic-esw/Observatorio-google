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
        word_freq[i] = word_freq[i]/len(document)
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

def sum_dictionarys(dict1):
    # Soma dois dicionarios
    counter = Counter()
    for d in dict1: 
        counter.update(d)
    return counter  

def create_top_frequency(documents):
    # Cria um dicionario com as frequências de todos os documentos
    array_freqs = []
    for i in documents:
        array_freqs.append(Counter(i))
    return (sum_dictionarys(array_freqs))

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

    # Ordena as listas top de forma decrescente
    top_frequency = create_top_frequency(documents)
    top_frequency = zip(top_frequency.values(),top_frequency.keys())    
    top_frequency = sorted(top_frequency)[::-1]
    top_frequency = [str(x[1]) + '(' + str(x[0]) + ')' for x in top_frequency[:num_palavras_chaves]]

    top_relevant  = zip(relevance_list.values(),relevance_list.keys())    
    top_relevant  = sorted(top_relevant)[::-1] 
    top_relevant  = [str(x[1]) + '(' + str(x[0])[:5] + ')' for x in top_relevant [:num_palavras_chaves]]
    
    
    # Retorna uma string contendo: 10 palavras mais relevantes e as 10 mais frequentes
    return (str(num_palavras_chaves) + " palavras mais relevantes: " + ', '.join(top_relevant) + '\n'
            )+ (str(num_palavras_chaves) + " palavras mais frequentes: " + ', '.join(top_frequency))
    
