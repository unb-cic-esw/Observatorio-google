from requirement import Requirement

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
