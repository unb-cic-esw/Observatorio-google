import pytest
import sys
sys.path.insert(0, sys.path[0] + "/../")
from adlink import AdLink

def test_adlink():
    
    adl = AdLink()
    assert adl.estado == 0
    assert adl._dados == []
     
    adl.shandletag('div',[('class','ad_cclk')])
    assert adl._dados == []
    assert adl.estado == 1
    
    adl.shandletag('h3',[])
    assert adl._dados == []
    assert adl.estado == 2

    adl.shandletag('a', [('style', 'display:none'),
     ('href', 'https://www.googleadservices.com/pagead/aclk?sa=L&amp;ai=DChcSEwiS2ov4xbjbAhUMDJEKHWrXA48YABAAGgJjZQ&amp;ohost=www.google.com.br&amp;cid=CAESEeD2Set0HttQt-TpSh70UmlV&amp;sig=AOD64_2dUa0gfSgR9WpLvMuRsFEG59hRUw&amp;q=&amp;ved=0ahUKEwjZjIf4xbjbAhWBnJAKHTr7CGwQ0QwIJw&amp;adurl='),
     ('id','n1s0p1c0')])
    assert adl.estado == 3
    assert adl._dados == []
    adl.ehandletag('a')
    assert adl.estado == 3
    assert adl._dados == []
    adl.shandletag('a', [('class', 'V0MxL r-i42tCLhf2sGM'),
                         ('href', 'mock'),
                         ('id', 'vn1s0p1c0')])

    assert adl.estado == 0
    assert adl._dados == ['mock']
    adl.ehandletag('a')
    assert adl.estado == 0
    assert adl._dados == ['mock']

    adl.ehandletag('h3')
    assert adl.estado == 0
    assert adl._dados == ['mock']

    adl.estado = 0
    adl.shandletag('z@@sakas@1',[('z@@sakas@1','z@@sakas@1')])
    assert adl.estado == 0
    assert adl._dados == ['mock']
    
    adl.estado = 1
    adl.shandletag('z@@sakas@1', [('z@@sakas@1', 'z@@sakas@1')])
    assert adl.estado == 0
    assert adl._dados == ['mock']
    
    adl.estado = 2
    adl.shandletag('z@@sakas@1', [('z@@sakas@1', 'z@@sakas@1')])
    assert adl.estado == 0
    assert adl._dados == ['mock']
    adl.estado = 3
    adl.shandletag('z@@sakas@1', [('z@@sakas@1', 'z@@sakas@1')])
    assert adl.estado == 0
    assert adl._dados == ['mock']