import pytest
import text_analyzer

def test_word_filter():
    string = "Frase a de o teste Lula , para"
    # Tira adverbios, artigos...
    assert text_analyzer.filter_words(string) == ["Frase", "teste", "Lula"]
    string = ""
    assert text_analyzer.filter_words(string) == []

def test_word_frequency():
    string = "a a a b b b b".split()
    dic = text_analyzer.word_frequency(string)
    assert dic['a'] == 3.0/7.0
    assert dic['b'] == 4.0/7.0

def test_create_top_frequency():
    stringa = "a a a b b b b".split()
    stringb = "a a a b b b b".split()
    freqs = text_analyzer.create_top_frequency([stringa,stringb])
    assert freqs['a'] == 6

def test_docs_appearences():
    stringa = "sal no almoço"
    stringb = "eu gosto de sal"
    # Sal aparece em dois documentos
    result  = text_analyzer.num_appearences_docs([stringa,stringb],"sal")
    assert  result == 2
    # Eu aparece em apenas um
    result  = text_analyzer.num_appearences_docs([stringa,stringb],"eu")
    assert  result == 1

def test_relevance():
    tf = {'a': 14, 'b':1}
    documents = ["a a a a a a a a", "b a a a a a a a"]
    idf = text_analyzer.inverse_word_frequency(documents,tf)
    # Como b aparece menos que a, sua relevância deve ser maior
    assert idf['b'] * tf['b'] > idf['a'] * tf['a']

def test_analyze():
    stringa = "Kiwi or kiwis are flightless birds native to New Zealand, in the genus Apteryx and  ratites "
    stringb = "family Apterygidae. Approximately the size of a domestic chicken, kiwi are by far the smallest living(which also consist of"
    stringc = "ostriches, emus, rheas, and cassowaries), and lay the largest egg in relation to their body size of any species of bird in the world"
    documents = [stringa,stringb,stringc]
    result  = text_analyzer.analyze(documents,4)
    assert result == "4 palavras mais relevantes: zealand(0.109), ratites(0.109), new(0.109), native(0.109)\n4 palavras mais frequentes: size(2), kiwi(2), zealand(1), world(1)"