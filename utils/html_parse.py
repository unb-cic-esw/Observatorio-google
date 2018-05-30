#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
import json


requirement = []
dictoutput = {}


class TopStoryImage():

	def __init__(self):
		self.nome = 'PrincipaisNoticiasImagens'
		self.dados = []
		self.contador = -1
		self.lista = ['g-img','img']

	def shandletag(self, tagin, attrs):
		if self.contador == -1:
			if tagin == 'div' and len(attrs) > 0 and attrs[0] == ('class', 'KNcnob'):
				self.contador = 0
		elif tagin == self.lista[self.contador]:
			self.contador += 1
		else:
			self.contador = -1
			
		if self.contador == 2:
			self.dados.append(attrs[1][1])
			self.contador = -1

	def ehandletag(self, tagin):
		pass

	def shandledata(self, data):
		pass

class AdPreview():
	def __init__(self):
		self.nome = 'previsaoPropagandas'
		self.dados = []
		self.dado = ""
		self.trigger = "div"
		self.outer_flag = False
		self.data_flag = False

	def shandletag(self, tagin, attrs):
		if not self.outer_flag:
			if tagin == self.trigger and ('class', 'ellip ads-creative') in attrs:
				self.outer_flag = True
				self.data_flag = True
		elif tagin == "div" and ('class','ellip') in attrs:
			self.data_flag = True
		elif not self.data_flag:
			self.outer_flag = False
			self.dados.append(self.dado)
			self.dado = ""
	def ehandletag(self, tagin):
		if tagin == "div" and self.data_flag:
			self.data_flag = False
	def shandledata(self, data):
		if self.data_flag:
			self.dado += data + ""
			

class AdTitle():
	def __init__(self):
		self.nome = 'tituloPropagandas'
		self.dados = []
		self.lista = ['div',
						'h3',
						'a',
						'a']
		self.estado = 0
		self.data_flag = False
	def shandletag(self, tagin, attrs):
		if self.estado == 0 and tagin == self.lista[0]:
			if ('class','ad_cclk') in attrs:
				self.estado += 1
		elif tagin == self.lista[self.estado]:
			self.estado += 1
			if(self.estado == len(self.lista)):
				self.data_flag = True
				self.estado = 0
		else:
			self.estado = 0
	def ehandletag(self, tagin):
		pass

	def shandledata(self, data):
		if self.data_flag:
			self.dados.append(data)
			self.data_flag = False


class AdLink():
	def __init__(self):
		self.nome = 'linkPropagandas'
		self.dados = []
		self.lista = ['div',
						'h3',
						'a',
						'a']
		self.estado = 0
	def shandletag(self, tagin, attrs):
		if self.estado == 0 and tagin == self.lista[0]:
			if ('class','ad_cclk') in attrs:
				self.estado += 1
		elif tagin == self.lista[self.estado]:
			self.estado += 1
			if(self.estado == len(self.lista)):
				self.dados.append(attrs[1][1])
				self.estado = 0
		else:
			self.estado = 0
	def ehandletag(self, tagin):
		pass

	def shandledata(self, data):
		pass


class SubResultTitle():
	def __init__(self):
		self.nome = 'tituloSubresultados'
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
		self.nome = 'linkSubresultados'
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


class ResultPreview():
	def __init__(self):
		self.nome = 'previsaoResultados'
		self.h3flag = False
		self.data_flag = False
		self.dados = []
		self.dado = ""
		self.spans_aninhados = 0

	def shandletag(self, tagin, attrs):
		if tagin == 'span' and ('class', 'st') in attrs:
			if self.spans_aninhados == 0:
				self.spans_aninhados += 1
				self.data_flag = True
		elif tagin == 'span' and self.data_flag:
			self.spans_aninhados += 1

	def ehandletag(self, tagin):
		if tagin == 'span' and self.data_flag:
			self.spans_aninhados -= 1
			if self.spans_aninhados == 0:
				self.dados.append(self.dado.strip())
				self.dado = ''
				self.data_flag = False


	def shandledata(self, data):
		if self.data_flag:
			self.dado += data

class ResultTitle() :
	def __init__(self):
		self.nome = 'tituloResultados'
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
		self.nome = 'linkResultados'
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

class TopStoryLink() :
	def __init__(self):
		self.tags = set()
		self.tags.add('g-inner-card')
		self.nome = 'linkNoticias'
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

class TopStoryTitle() :
	def __init__(self):
		self.tags = set()
		self.tags.add('div')
		self.nome = 'tituloNoticias'
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

requirement.append(TopStoryImage())
requirement.append(TopStoryTitle())
requirement.append(TopStoryLink())
requirement.append(ResultLink())
requirement.append(ResultTitle())
requirement.append(ResultPreview())
requirement.append(SubResultTitle())
requirement.append(SubResultLink())
requirement.append(AdLink())
requirement.append(AdTitle())
requirement.append(AdPreview())

parser = MyParser()

filename = input()

with open(filename + ".html") as f:
    parser.feed(f.read())

json_string = "{"
for req in requirement:
	if(json_string[-1] != '{'):
		json_string += ","
	req.nome = req.nome.replace("\"", "\\\"")
	json_string += "\"" + req.nome + "\"" + ": ["
	for dado in req.dados:
		if(json_string[-1] != '['):
			json_string += ","
		dado = dado.replace("\"", "\\\"")
		json_string += "\"" + dado + "\""
	json_string += "]"		
json_string += "}"

print(json_string)

# filename += ".json"
# ftry = open(filename,"w+")

# # If the file name exists, write a JSON string into the file.
# if filename:
#     # Writing JSON data
#     with ftry as f:
#         json.dump(dictoutput, f)
