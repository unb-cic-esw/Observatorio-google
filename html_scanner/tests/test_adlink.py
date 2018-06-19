import pytest
import sys
sys.path.insert(0, sys.path[0] + "/../")
from adlink import AdLink

intest1 = [('div',[('class','ad_cclk')]),
            ('h3',[('class','ad_cclk')]),
            (' ',[('class','ad_cclk')]),
            ('div',[('class',' ')]),
            ('div',[(' ','ad_cclk')]),
            (' ',[(' ',' ')])
            ]

intest2 = [('h3',[]), 
            ('a', []), 
            (' ', []), 
            ('h3', [('class','ad_cclk')])
            ]

intest3 = [('a', [('style', 'display:none'), ('href', 'https://www.googleadservices.com/pagead/aclk?sa=L&amp;ai=DChcSEwiS2ov4xbjbAhUMDJEKHWrXA48YABAAGgJjZQ&amp;ohost=www.google.com.br&amp;cid=CAESEeD2Set0HttQt-TpSh70UmlV&amp;sig=AOD64_2dUa0gfSgR9WpLvMuRsFEG59hRUw&amp;q=&amp;ved=0ahUKEwjZjIf4xbjbAhWBnJAKHTr7CGwQ0QwIJw&amp;adurl='), ('id','n1s0p1c0')]), 
            (' ', [('style', 'display:none'), ('href', 'https://www.googleadservices.com/pagead/aclk?sa=L&amp;ai=DChcSEwiS2ov4xbjbAhUMDJEKHWrXA48YABAAGgJjZQ&amp;ohost=www.google.com.br&amp;cid=CAESEeD2Set0HttQt-TpSh70UmlV&amp;sig=AOD64_2dUa0gfSgR9WpLvMuRsFEG59hRUw&amp;q=&amp;ved=0ahUKEwjZjIf4xbjbAhWBnJAKHTr7CGwQ0QwIJw&amp;adurl='), ('id','n1s0p1c0')]), 
            ('a', [('href', 'https://www.googleadservices.com/pagead/aclk?sa=L&amp;ai=DChcSEwiS2ov4xbjbAhUMDJEKHWrXA48YABAAGgJjZQ&amp;ohost=www.google.com.br&amp;cid=CAESEeD2Set0HttQt-TpSh70UmlV&amp;sig=AOD64_2dUa0gfSgR9WpLvMuRsFEG59hRUw&amp;q=&amp;ved=0ahUKEwjZjIf4xbjbAhWBnJAKHTr7CGwQ0QwIJw&amp;adurl='), ('style', 'display:none'), ('id','n1s0p1c0')]), 
            ('a', [('id','n1s0p1c0'), ('href', 'https://www.googleadservices.com/pagead/aclk?sa=L&amp;ai=DChcSEwiS2ov4xbjbAhUMDJEKHWrXA48YABAAGgJjZQ&amp;ohost=www.google.com.br&amp;cid=CAESEeD2Set0HttQt-TpSh70UmlV&amp;sig=AOD64_2dUa0gfSgR9WpLvMuRsFEG59hRUw&amp;q=&amp;ved=0ahUKEwjZjIf4xbjbAhWBnJAKHTr7CGwQ0QwIJw&amp;adurl='), ('style', 'display:none')]), 
            ('a', [(' '), (' '), (' ')]), 
            ('a', [(' '), (' '), ('class','ad_cclk')])
            ]

intest4 = [('a'),
            (' ')
            ]

intest5 = [('a', [('class', 'V0MxL r-i42tCLhf2sGM'), ('href', 'mock'), ('id', 'vn1s0p1c0')]), 
            ('a', [('style', 'display:none'), ('href', 'https://www.googleadservices.com/pagead/aclk?sa=L&amp;ai=DChcSEwiS2ov4xbjbAhUMDJEKHWrXA48YABAAGgJjZQ&amp;ohost=www.google.com.br&amp;cid=CAESEeD2Set0HttQt-TpSh70UmlV&amp;sig=AOD64_2dUa0gfSgR9WpLvMuRsFEG59hRUw&amp;q=&amp;ved=0ahUKEwjZjIf4xbjbAhWBnJAKHTr7CGwQ0QwIJw&amp;adurl='), ('id','n1s0p1c0')]), 
            (' ', [('style', 'display:none'), ('href', 'https://www.googleadservices.com/pagead/aclk?sa=L&amp;ai=DChcSEwiS2ov4xbjbAhUMDJEKHWrXA48YABAAGgJjZQ&amp;ohost=www.google.com.br&amp;cid=CAESEeD2Set0HttQt-TpSh70UmlV&amp;sig=AOD64_2dUa0gfSgR9WpLvMuRsFEG59hRUw&amp;q=&amp;ved=0ahUKEwjZjIf4xbjbAhWBnJAKHTr7CGwQ0QwIJw&amp;adurl='), ('id','n1s0p1c0')]), 
            ('a', [('href', 'https://www.googleadservices.com/pagead/aclk?sa=L&amp;ai=DChcSEwiS2ov4xbjbAhUMDJEKHWrXA48YABAAGgJjZQ&amp;ohost=www.google.com.br&amp;cid=CAESEeD2Set0HttQt-TpSh70UmlV&amp;sig=AOD64_2dUa0gfSgR9WpLvMuRsFEG59hRUw&amp;q=&amp;ved=0ahUKEwjZjIf4xbjbAhWBnJAKHTr7CGwQ0QwIJw&amp;adurl='), ('style', 'display:none'), ('id','n1s0p1c0')]), 
            ('a', [(' '), (' '), (' ')]), 
            ('a', [(' '), (' '), ('class','ad_cclk')])
            ]

def test_adlink():
    adl = AdLink()
    #assert adl.estado == 0
    assert adl._dados == []     
    for i in intest1:
        adl.shandletag(intest1[i])
        for j in intest2:
            adl.shandletag(intest2[j])
            for k in intest3:
                adl.shandletag(intest3[k])
                for l in intest4:
                    adl.ehandletag(intest4[l])
                    for m in intest2:
                        adl.shandletag(intest5[m])
                        if intest1[i][0] == ('div') and intest1[i][1] == ('class', 'ad_cclk'):
                            if intest2[j][0] == ('h3'):
                                if intest3[k][0] == ('a'):
                                    if intest4[k] == ('a'): #really don´t care in this version
                                        if intest5[k][0] == ('a'):
                                            assert adl._dados[-1] == intest5[1][1] #-1 para buscar ultimo elemento
                                        else:
                                            assert not adl._dados[-1] == intest5[1][1]
                                    else:
                                        if intest5[k][0] == ('a'):
                                            assert adl._dados[-1] == intest5[1][1]
                                        else:
                                            assert not adl._dados[-1] == intest5[1][1]
                                else:
                                    assert not adl._dados[-1] == intest5[1][1]
                            else:
                                assert not adl._dados[-1] == intest5[1][1]
                        else:
                            assert not adl._dados[-1] == intest5[1][1]
assert adl.estado == 0
