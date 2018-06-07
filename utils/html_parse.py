#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from topstory import TopStory
from genericresult import GenericResult
import json

# import .requirement


requirement = []
dictoutput = {}

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

try:
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


	json_string = json.dumps(dictoutput)
	print(json_string)
except:
	print("{}")
	# filename += ".json"
	# ftry = open(filename,"w+")

	# # If the file name exists, write a JSON string into the file.
	# if filename:
	#     # Writing JSON data
	#     with ftry as f:
	#         json.dump(dictoutput, f)

