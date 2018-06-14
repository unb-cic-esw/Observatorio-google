import pytest
import sys
sys.path.insert(0, sys.path[0] + "/../")
from adpreview import AdPreview

def test_adlink():
    adp = AdPreview()
    assert adp._dados == []
    assert adp.data_flag == False
    assert adp.outer_flag == False
    
    adp.shandletag('div', [('class', 'I6vAHd h5RoYd ads-creative')])
    assert adp.outer_flag == True
    assert adp.data_flag == True
    assert adp.dado == ""
    
    adp.shandledata('Invista com os especialistas da XP! ')
    assert adp.dado == 'Invista com os especialistas da XP! '
    assert adp.outer_flag == True
    assert adp.data_flag == True
    
    adp.shandletag('b',[])
    assert adp.data_flag == True
    assert adp.outer_flag == True
    assert adp.dado == 'Invista com os especialistas da XP! '
    
    adp.shandledata('Investimentos')
    assert adp.data_flag == True
    assert adp.outer_flag == True
    assert adp.dado == 'Invista com os especialistas da XP! Investimentos'
    
    st = adp.dado
    adp.ehandletag('b')
    adp.shandledata('mock')
    st += 'mock'
    assert st == adp.dado
    assert adp.data_flag == True
    assert adp.outer_flag == True
    adp.ehandletag('div')
    assert adp._dados == []
    assert adp.dado == st
    assert adp.data_flag == False
    assert adp.outer_flag == True
    adp.shandletag('div',[('class','rc')])
    assert adp.dado == ''
    assert adp._dados == [st]
    assert adp.outer_flag == False
    