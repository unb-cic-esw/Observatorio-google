from compositerequirement import CompositeRequirement
from adtitle import AdTitle
from adlink import AdLink
from adpreview import AdPreview



class Ad(CompositeRequirement):
	def __init__(self):
		self._nome = 'Ad'
		self._dados = []
		self.lista = []
		self.lista.append(AdTitle())
		self.lista.append(AdLink())
		self.lista.append(AdPreview())
