#!/usr/bin/env python3
# -*- coding: utf-8 -*

from html.parser import HTMLParser
from topstory import TopStory
from genericresult import GenericResult
import json


# Essa classe separa o html para fornecer entradas aos scanners
class MyParser(HTMLParser):

	def addRequirement(self,req):
		self.lista.append(req)

	def run(self,htmlString):
		self.feed(htmlString)
		dictoutput = {}

		for i in range(len(self.lista)):
			req = self.lista[i]
			dictoutput[req.nome()] = req.dados()

		return dictoutput
		
	def __init__(self):
		self.flag = False
		super(MyParser, self).__init__()
		self.lista = []

	def handle_starttag(self, tag, attrs):
		for req in self.lista:
			req.shandletag(tag, attrs)

	def handle_endtag(self, tag):
		for req in self.lista:
			req.ehandletag(tag)

	def handle_data(self, data):
		for req in self.lista:
			req.shandledata(data)

def extract_info(htmlString):
	try:
		
		parser = MyParser()

		parser.addRequirement(TopStory())
		parser.addRequirement(GenericResult())

		return parser.run(htmlString)
	except:
		return json.loads("{}")

if __name__ == "__main__":
	with open("../teste.html") as f:
		parser = MyParser()
		parser.addRequirement(TopStory())
		parser.addRequirement(GenericResult())
		print(parser.run(f.read()))