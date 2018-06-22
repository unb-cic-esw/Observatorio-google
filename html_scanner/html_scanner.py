#!/usr/bin/env python3
# -*- coding: utf-8 -*

import json
from html.parser import HTMLParser
from topstory import TopStory
from genericresult import GenericResult

# Essa classe separa o html para fornecer entradas aos scanners
class MyParser(HTMLParser):

    def add_requirement(self, req):
        self.lista.append(req)

    def run(self, html_string):
        self.feed(html_string)
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

def extract_info(html_string):
    try:

        parser = MyParser()

        parser.add_requirement(TopStory())
        parser.add_requirement(GenericResult())

        return parser.run(html_string)
    except:
        return json.loads("{}")

def main():
    with open("../teste.html") as file:
        parser = MyParser()
        parser.add_requirement(TopStory())
        parser.add_requirement(GenericResult())
        print(parser.run(file.read()))

if __name__ == "__main__":
    main()
