#!/usr/bin/env python3
# -*- coding: utf-8 -*

from html.parser import HTMLParser
from topstory import TopStory
from genericresult import GenericResult
import json

requirement = []
dictoutput = {}

# Essa classe separa o html para fornecer entradas aos scanners
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

def extract_info(htmlString):
	try:
		requirement.append(TopStory())
		requirement.append(GenericResult())
		# requirement.append(Result())

		# requirement.append(Ad())


		parser = MyParser()

		parser.feed(htmlString)

		json_string = "{"
		for i in range(len(requirement)):
			req = requirement[i]
			dictoutput[req.nome()] = req.dados()
		
		return dictoutput
	except:
		return json.loads("{}")
