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
