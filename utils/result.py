from compositerequirement import CompositeRequirement
from resulttitle import ResultTitle
from resultlink import ResultLink
from resultpreview import ResultPreview
from subresultlist import SubResultList

class Result(CompositeRequirement):
	def __init__(self):
		self._nome = 'Resultado'
		self._dados = []
		self.lista = []
		self.lista.append(ResultTitle())
		self.lista.append(ResultLink())
		self.lista.append(ResultPreview())
		self.lista.append(SubResultList())

