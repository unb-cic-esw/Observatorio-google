#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
import json


requirement = []
dictoutput = {}


class Requirement():

	def __init__(self):
		self._dados = None
		self._nome = None

	def dados(self):
		return self._dados

	def nome(self):
		return self._nome

class CompositeRequirement(Requirement):
	def __init__(self):
		super(CompositeRequirement, self).__init__()
		self.lista = []
	
	def dados(self):
		for i in range(0, len(self.lista[0].dados())):
			acc = {}
			for req in self.lista:
				acc[req.nome()] = req.dados()[i]
			self._dados.append(acc)
		return self._dados

	def shandletag(self, tagin, attrs):
		for req in self.lista:
			req.shandletag(tagin, attrs)

	def ehandletag(self, tagin):
		for req in self.lista:
			req.ehandletag(tagin)

	def shandledata(self, data):
		for req in self.lista:
			req.shandledata(data)

class GenericResult(CompositeRequirement):

	def __init__(self):
		self._nome = 'Resultado'
		self._dados = []
		self.lista = []
		self.lista.append(Ad())
		self.lista.append(Result())

	def dados(self):
		for item in self.lista[0].dados():
			acc = item
			item["is_ad"] = True
			self._dados.append(acc)

		for item in self.lista[1].dados():
			acc = item
			item["is_ad"] = False
			self._dados.append(acc)
		return self._dados

class TopStory(CompositeRequirement):
	def __init__(self):
		self._nome = 'PrincipaisNoticias'
		self._dados = []
		self.lista = []
		self.lista.append(TopStoryTitle())
		self.lista.append(TopStoryLink())
		self.lista.append(TopStoryImage())
		# self.lista.append(subresultados())
		
		

class TopStoryImage(Requirement):

	def __init__(self):
		self._nome = 'PrincipaisNoticiasImagens'
		self._dados = []
		self.contador = -1
		self.lista = ['g-img', 'img']

	def shandletag(self, tagin, attrs):
		if self.contador == -1:
			if tagin == 'div' and len(attrs) > 0 and attrs[0] == ('class', 'KNcnob'):
				self.contador = 0
		elif tagin == self.lista[self.contador]:
			self.contador += 1
		else:
			self.contador = -1

		if self.contador == 2:
			self._dados.append(attrs[1][1])
			self.contador = -1

	def ehandletag(self, tagin):
		pass

	def shandledata(self, data):
		pass


class TopStoryLink(Requirement):
	def __init__(self):
		self.tags = set()
		self.tags.add('g-inner-card')
		self._nome = 'linkNoticias'
		self.gflag = False
		self._dados = []

	def shandletag(self, tagin, attrs):
		if self.gflag:
			if tagin == 'a':
				self._dados.append(attrs[0][1])
			self.gflag = False
		elif tagin in self.tags:
			self.gflag = True

	def ehandletag(self, tagin):
		return

	def shandledata(self, data):
		return


class TopStoryTitle(Requirement):
	def __init__(self):
		self.tags = set()
		self.tags.add('div')
		self._nome = 'tituloNoticias'
		self.flag = False
		self.atributos = set()
		self.atributos.add(('style', '-webkit-line-clamp:4;height:5.5em'))
		self._dados = []

	def shandletag(self, tagin, attrs):
		if tagin in self.tags:
			aux = [tagin]
			for attr in attrs:
				if attr in self.atributos:
					aux += [attr]
			if len(aux) > 1:
				self.flag = True

	def ehandletag(self, tagin):
		return

	def shandledata(self, data):
		if self.checkflag():
			self._dados.append(data)

	def checkflag(self):
		if self.flag:
			self.flag = False
			return True
		else:
			return self.flag


class Ad(CompositeRequirement):
	def __init__(self):
		self._nome = 'Ad'
		self._dados = []
		self.lista = []
		self.lista.append(AdTitle())
		self.lista.append(AdLink())
		self.lista.append(AdPreview())





class AdTitle(Requirement):
	def __init__(self):
		self._nome = 'tituloPropagandas'
		self._dados = []
		self.lista = ['div',
                    'h3',
                    'a',
                    'a']
		self.estado = 0
		self.data_flag = False

	def shandletag(self, tagin, attrs):
		if self.estado == 0 and tagin == self.lista[0]:
			if ('class', 'ad_cclk') in attrs:
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
			self._dados.append(data)
			self.data_flag = False


class AdLink(Requirement):
	def __init__(self):
		self._nome = 'linkPropagandas'
		self._dados = []
		self.lista = ['div',
                    'h3',
                    'a',
                    'a']
		self.estado = 0

	def shandletag(self, tagin, attrs):
		if self.estado == 0 and tagin == self.lista[0]:
			if ('class', 'ad_cclk') in attrs:
				self.estado += 1
		elif tagin == self.lista[self.estado]:
			self.estado += 1
			if(self.estado == len(self.lista)):
				self._dados.append(attrs[1][1])
				self.estado = 0
		else:
			self.estado = 0

	def ehandletag(self, tagin):
		pass

	def shandledata(self, data):
		pass

class AdPreview(Requirement):
	def __init__(self):
		self._nome = 'previsaoPropagandas'
		self._dados = []
		self.dado = ""
		self.trigger = "div"
		self.outer_flag = False
		self.data_flag = False

	def checkTrigger(self,attrs):
		for attr in attrs:
			if attr[0] == 'class' and 'ads-creative' in attr[1]:
				return True
		return False

	def shandletag(self, tagin, attrs):
		if not self.outer_flag:
			
			if tagin == self.trigger and self.checkTrigger(attrs):	
				self.outer_flag = True
				self.data_flag = True
		elif tagin == "div" and ('class', 'ellip') in attrs:
			self.data_flag = True
		elif not self.data_flag:
			self.outer_flag = False
			self._dados.append(self.dado)
			self.dado = ""

	def ehandletag(self, tagin):
		if tagin == "div" and self.data_flag:
			self.data_flag = False

	def shandledata(self, data):
		if self.data_flag:
			self.dado += data + ""

class SubResultList(Requirement):

	def __init__(self):
		self._nome = 'ListaSubResultados'
		self._dados = []
		self.h3flag = False
		self.first_cut = False

		self.subr = SubResult()

	def dados(self):
		self.cutList()
		return self._dados

	def cutList(self):
		if self.first_cut:
			self._dados.append(self.subr.dados())
			self.subr = SubResult()
		else:
			self.first_cut = True

	def shandletag(self, tagin, attrs):
		self.subr.shandletag(tagin,attrs)
		if self.h3flag:
			if tagin == 'a':
				if attrs[0][0] == 'href':
					self.cutList()
			self.h3flag = False
		else:
			if tagin == 'h3':
				for attr in attrs:
					if attr == ('class', 'r'):
						self.h3flag = True

	def ehandletag(self, tagin):
		self.subr.ehandletag(tagin)

	def shandledata(self, data):
		self.subr.shandledata(data)
		

	def checkflag(self):
		return

class SubResult(CompositeRequirement):
	def __init__(self):
		self._nome = 'SubResultado'
		self._dados = []
		self.lista = []
		self.lista.append(SubResultTitle())
		self.lista.append(SubResultLink())



class SubResultTitle(Requirement):
	def __init__(self):
		self._nome = 'tituloSubresultados'
		self.data_flag = False
		self._dados = []
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
			self._dados.append(data)
			self.data_flag = False


class SubResultLink(Requirement):
	def __init__(self):
		self._nome = 'linkSubresultados'
		self._dados = []
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
				self._dados.append(attrs[1][1])
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

class Result(CompositeRequirement):
	def __init__(self):
		self._nome = 'Resultado'
		self._dados = []
		self.lista = []
		self.lista.append(ResultTitle())
		self.lista.append(ResultLink())
		self.lista.append(ResultPreview())
		self.lista.append(SubResultList())



class ResultPreview(Requirement):
	def __init__(self):
		self._nome = 'previsaoResultados'
		self.h3flag = False
		self.data_flag = False
		self._dados = []
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
				self._dados.append(self.dado.strip())
				self.dado = ''
				self.data_flag = False

	def shandledata(self, data):
		if self.data_flag:
			self.dado += data


class ResultTitle(Requirement):
	def __init__(self):
		self._nome = 'tituloResultados'
		self._dados = []
		self.h3flag = False
		self.dflag = False

	def shandletag(self, tagin, attrs):
		if self.h3flag:
			if tagin == 'a':
				if attrs[0][0] == 'href':
					self.dflag = True
			self.h3flag = False
		else:
			if tagin == 'h3':
				for attr in attrs:
					if attr == ('class', 'r'):
						self.h3flag = True
					

	def ehandletag(self, tagin):
		return

	def shandledata(self, data):
		if self.dflag:
			self._dados.append(data)
			self.dflag = False

	def checkflag(self):
		return


class ResultLink(Requirement):
	def __init__(self):
		self._nome = 'linkResultados'
		self.h3flag = False
		self._dados = []

	def shandletag(self, tagin, attrs):
		if self.h3flag:
			if tagin == 'a':
				if attrs[0][0] == 'href':
					self._dados.append(attrs[0][1])
			self.h3flag = False
		else:
			if tagin == 'h3':
				for attr in attrs:
					if attr == ('class', 'r'):
						self.h3flag = True

	def ehandletag(self, tagin):
		return

	def shandledata(self, data):
		return

	def checkflag(self):
		return



class MyParser(HTMLParser):
	def __init__(self):
		self.flag = False
		super(MyParser, self).__init__()

	def handle_starttag(self, tag, attrs):
		for req in requirement:
			req.shandletag(tag, attrs)

	def handle_endtag(self, tag):
		for req in requirement:
			req.ehandletag(tag)

	def handle_data(self, data):
		for req in requirement:
			req.shandledata(data)


requirement.append(TopStory())
requirement.append(GenericResult())
# requirement.append(Result())

# requirement.append(Ad())


parser = MyParser()

filename = input()

with open(filename + ".html") as f:
    parser.feed(f.read())

json_string = "{"
for i in range(len(requirement)):
	req = requirement[i]
	dictoutput[req.nome()] = req.dados()

# print(requirement)
# print(dictoutput)

# filename += ".json"

# ftry = open(filename,"w+")

# If the file name exists, write a JSON string into the file.
# if filename:
    # Writing JSON data
    # wit/h ftry as f:

# 	if(json_string[-1] != '{'):
# 		json_string += ","
# 	req.nome = req.nome.replace("\"", "\\\"")
# 	json_string += "\"" + req.nome + "\"" + ": ["
# 	for dado in req.dados:
# 		if(json_string[-1] != '['):
# 			json_string += ","
# 		dado = dado.replace("\"", "\\\"")
# 		json_string += "\"" + dado + "\""
# 	json_string += "]"
# json_string += "}"

json_string = json.dumps(dictoutput)
print(json_string)

# filename += ".json"
# ftry = open(filename,"w+")

# # If the file name exists, write a JSON string into the file.
# if filename:
#     # Writing JSON data
#     with ftry as f:
#         json.dump(dictoutput, f)

