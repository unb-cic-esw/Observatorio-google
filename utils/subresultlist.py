from requirement import Requirement
from subresult import SubResult 

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
