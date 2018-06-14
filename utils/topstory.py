from compositerequirement import CompositeRequirement

from topstorytitle import TopStoryTitle
from topstorylink import  TopStoryLink
from topstoryimage import  TopStoryImage

# Essa classe representa os dados de uma principal noticia

class TopStory(CompositeRequirement):
	def __init__(self):
		self._nome = 'PrincipaisNoticias'
		self._dados = []
		self.lista = []
		self.lista.append(TopStoryTitle())
		self.lista.append(TopStoryLink())
		self.lista.append(TopStoryImage())
		# self.lista.append(subresultados())
