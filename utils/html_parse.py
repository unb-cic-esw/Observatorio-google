from html.parser import HTMLParser
import json


requirement = []
dictoutput = {}

class SubResultTitle():
	def __init__(self):
		self.nome = 'Titulo SubResultado'
		self.data_flag = False
		self.dados = []
		self.lista = ["table",
						"tr",
						"td",
						"div",
						"span",
						"h3",
						"a",
						"div",
						"div",
						"br"]
		self.estado = 0

	def shandletag(self, tagin, attrs):
		if tagin == self.lista[self.estado]:
			if self.estado == 6:
				self.data_flag = True
			self.estado += 1
			if self.estado >= len(self.lista):
				self.estado = 2			
		else:
			self.estado = 0

	def ehandletag(self, tagin):
		if tagin == "tr" and self.estado > 0:
			self.estado = 1

	def shandledata(self, data):
		if self.data_flag:
			self.dados.append(data)
			self.data_flag = False


class SubResultLink():
	def __init__(self):
		self.nome = 'Titulo SubResultado'
		self.dados = []
		self.lista = [
						'table',
						'tr',
						'td',
						'div',
						'span',
						'h3',
						'a',
						'div',
						'div',
						'br']
		self.estado = 0

	def shandletag(self, tagin, attrs):
		if tagin == self.lista[self.estado]:
			if self.estado == 6:
				self.dados.append(attrs[1][1])
			self.estado += 1
			if self.estado >= len(self.lista):
				self.estado = 2			
		else:
			self.estado = 0

	def ehandletag(self, tagin):
		if tagin == "tr" and self.estado > 0:
			self.estado = 1

	def shandledata(self, data):
		pass

class ResultTitle() :
	def __init__(self):
		self.nome = 'Titulo Resultado'
		self.h3flag = False
		self.dflag = False
		self.dados = []

	def shandletag(self, tagin, attrs):
		if self.h3flag:
			if tagin == 'a':
				if attrs[0][0] == 'href':
					self.dflag = True
			self.h3flag = False
			self.rcflag = False
		else:
			if tagin == 'h3':
				for attr in attrs:
					if attr == ('class', 'r'):
						self.h3flag = True
					else:
						self.rcflag = False
			else:
				self.rcflag = False

	def ehandletag(self, tagin):
		return

	def shandledata(self, data):
		if self.dflag:
			self.dados.append(data)
			self.dflag = False

	def checkflag(self):
		return

class ResultLink() :
	def __init__(self):
		self.nome = 'link Resultado'
		self.h3flag = False
		self.dados = []

	def shandletag(self, tagin, attrs):
		if self.h3flag:
			if tagin == 'a':
				if attrs[0][0]=='href':
					self.dados.append(attrs[0][1])
			self.h3flag = False
			self.rcflag = False
		else:
			if tagin == 'h3':
				for attr in attrs:
					if attr == ('class', 'r'):
						self.h3flag = True
					else:
						self.rcflag = False
			else:
				self.rcflag = False

	def ehandletag(self, tagin):
		return

	def shandledata(self, data):
		return

	def checkflag(self):
		return

class TopStoriesLink() :
	def __init__(self):
		self.tags = set()
		self.tags.add('g-inner-card')
		self.nome = 'link Top Stories'
		self.gflag = False
		self.dados = []

	def shandletag(self, tagin, attrs):
		if self.gflag:
			if tagin == 'a':
				self.dados.append(attrs[0][1])
			self.gflag = False
		elif tagin in self.tags:
			self.gflag = True

	def ehandletag(self, tagin):
		return

	def shandledata(self, data):
		return

class TopStoriesTitle() :
	def __init__(self):
		self.tags = set()
		self.tags.add('div')
		self.nome = 'Titulo Top Stories'
		self.flag = False
		self.atributos = set()
		self.atributos.add(('style','-webkit-line-clamp:4;height:5.5em'))
		self.dados = []

	def shandletag(self, tagin, attrs):
		if tagin in self.tags:
			aux=[tagin]
			for attr in attrs:
				if attr in self.atributos:
					aux += [attr]
			if len(aux) > 1:
				self.flag = True

	def ehandletag(self, tagin):
		return

	def shandledata(self, data):
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
		for req in requirement:
			req.shandletag(tag, attrs)

	def handle_endtag(self, tag):
		for req in requirement:
			req.ehandletag(tag)

	def handle_data(self, data):
		for req in requirement:
			req.shandledata(data)

requirement.append(TopStoriesTitle())
requirement.append(TopStoriesLink())
requirement.append(ResultLink())
requirement.append(ResultTitle())
requirement.append(SubResultTitle())
requirement.append(SubResultLink())

parser = MyParser()

with open("../teste.html") as f:
    parser.feed(f.read())


# for registro in lista:
#     print(registro)
for req in requirement:
	dictoutput[req.nome] = req.dados
json_string = json.dumps(dictoutput)
filename = "../teste.json"
ftry = open(filename,"w+")

# If the file name exists, write a JSON string into the file.
if filename:
    # Writing JSON data
    with ftry as f:
        json.dump(json_string, f)