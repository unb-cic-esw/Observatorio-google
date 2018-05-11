from html.parser import HTMLParser


lista = []


tags = set()

tags.add('h3')
tags.add('a')
tags.add('div')


atributos = set()
atributos.add(('style','-webkit-line-clamp:4;height:5.5em'))

dados = []

class MyParser(HTMLParser):

    
    def __init__(self):
        self.flag = False
        super(MyParser,self).__init__()

    def handle_starttag(self, tag, attrs):
        aux = [tag]
        if tag in tags:
            for attr in attrs:
                if attr in atributos:
                    aux += [attr]
            if len(aux) > 1:
                lista.append(tuple(aux))
                self.flag = True

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if self.flag:
            dados.append(data)
            self.flag = False


parser = MyParser()

with open("../resultados/2018-5-10/teste.html") as f:
    parser.feed(f.read())


# for registro in lista:
#     print(registro)

for dado in dados:
    print(dado)