import pytest
import sys
sys.path.insert(0, sys.path[0] + "/../")
from adtitle import AdTitle

def test_adtitle():
    adt = AdTitle()
    assert adt.estado == 0
    assert adt._dados == []
    assert adt.data_flag == False

    adt.shandletag('div', [('class', 'ad_cclk')])
    assert adt._dados == []
    assert adt.estado == 1
    assert adt.data_flag == False
    adt.shandletag('h3', [])
    assert adt._dados == []
    assert adt.estado == 2
    assert adt.data_flag == False
    adt.shandletag('a', [('style', 'display:none'),
                         ('href', 'https://www.googleadservices.com/pagead/aclk?sa=L&amp;ai=DChcSEwiS2ov4xbjbAhUMDJEKHWrXA48YABAAGgJjZQ&amp;ohost=www.google.com.br&amp;cid=CAESEeD2Set0HttQt-TpSh70UmlV&amp;sig=AOD64_2dUa0gfSgR9WpLvMuRsFEG59hRUw&amp;q=&amp;ved=0ahUKEwjZjIf4xbjbAhWBnJAKHTr7CGwQ0QwIJw&amp;adurl='),
                         ('id', 'n1s0p1c0')])
    assert adt.estado == 3
    assert adt._dados == []
    assert adt.data_flag == False

    adt.ehandletag('a')
    assert adt.estado == 3
    assert adt._dados == []
    assert adt.data_flag == False
    adt.shandletag('a', [('class', 'V0MxL r-i42tCLhf2sGM'),
                         ('href', 'mock'),
                         ('id', 'vn1s0p1c0')])

    assert adt.estado == 0
    assert adt._dados == []
    assert adt.data_flag == True
    adt.shandledata(
        'mock')
    assert adt._dados == ['mock']
    assert adt.estado == 0
    assert adt.estado == adt.data_flag == False
     
    adt.ehandletag('a')
    assert adt.estado == 0
    assert adt._dados == ['mock']

    adt.ehandletag('h3')
    assert adt.estado == 0
    assert adt._dados == ['mock']

    adt.estado = 0
    adt.shandletag('z@@sakas@1', [('z@@sakas@1', 'z@@sakas@1')])
    assert adt.estado == 0
    assert adt._dados == ['mock']

    adt.estado = 1
    adt.shandletag('z@@sakas@1', [('z@@sakas@1', 'z@@sakas@1')])
    assert adt.estado == 0
    assert adt._dados == ['mock']

    adt.estado = 2
    adt.shandletag('z@@sakas@1', [('z@@sakas@1', 'z@@sakas@1')])
    assert adt.estado == 0
    assert adt._dados == ['mock']
    adt.estado = 3
    adt.shandletag('z@@sakas@1', [('z@@sakas@1', 'z@@sakas@1')])
    assert adt.estado == 0
    assert adt._dados == ['mock']

    adt.data_flag = False
    adt.shandledata('aba')
    assert adt._dados == ['mock']