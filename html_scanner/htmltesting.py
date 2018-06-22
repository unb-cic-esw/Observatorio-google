from html.parser import HTMLParser


requirement = []

class TopStoriesLink() :
    def __init__(self):
        self.tags = set()
        self.tags.add('g-inner-card')
        self.nome = 'link Top Stories'
        self.gflag = False
        self.flag = False
        self.atributos = set()
        self.atributos.add(('style','-webkit-line-clamp:4;height:5.5em'))
        self.dados = []

    def shandletag(self, tagin, attrs):
        # print("found a tag")
        # print(tagin)
        # print('\t' + str(attrs))
        if self.gflag:
            if tagin == 'a':
                self.dados.append(attrs[0])
            else:
                self.gflag = False
        elif tagin in self.tags:
            self.gflag = True

    def ehandletag(self, tagin):
        # print("found end tag")
        # print(tagin)
        return

    def shandledata(self, data):
        # print("found data")
        # print(data)
        if self.checkflag():
            self.dados.append(data)

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

    def handle_starttag(self, tag, attrs):
        print ('begin found a ' + tag)
        print ("plus ")
        for attr in attrs:
            print(attr)
        for req in requirement:
            req.shandletag(tag, attrs)

    def handle_endtag(self, tag):
        print ('end found a ' + tag)
        for req in requirement:
            req.ehandletag(tag)

    def handle_data(self, data):
        print ('data ' + data)
        for req in requirement:
            req.shandledata(data)

requirement.append(TopStoriesLink())

parser = MyParser()

with open("../outro_html.html") as f:
    parser.feed(f.read())


# for registro in lista:
#     print(registro)
for req in requirement:
    print (req.nome + ':')
    for dado in req.dados:
        print(dado)