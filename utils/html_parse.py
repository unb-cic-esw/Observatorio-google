from html.parser import HTMLParser


lista = []


tags = set()

tags.add('h3')
tags.add('a')
tags.add('div')


atributos = set()
atributos.add(('style','-webkit-line-clamp:4;height:5.5em'))

dados = []

class HighLevelReq() :
    def __init__(self):
        self.tag = 'div'
        self.nome = 'resultado top stories'
        self.flag = False
        self.atributos = set()
        self.atributos.add(('style','-webkit-line-clamp:4;height:5.5em'))

    def checkval(self, attrs):
        aux=[self.tag]
        for attr in attrs:
            if attr in self.atributos:
                aux += [attr]
        if len(aux) > 1:
            lista.append(tuple(aux))
            self.flag = True

    def checkflag(self):
    	if self.flag:
    		self.flag=False
    		return True
    	else:
    		return self.flag

class MyParser(HTMLParser):

    
    def __init__(self):
        self.flag = False
        super(MyParser,self).__init__()
        self.requirement = HighLevelReq()

    def handle_starttag(self, tag, attrs):
        if tag in tags:
        	self.requirement.checkval(attrs)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if self.requirement.checkflag():
            dados.append(data)


parser = MyParser()

with open("../teste.html") as f:
    parser.feed(f.read())


# for registro in lista:
#     print(registro)

for dado in dados:
    print(dado)