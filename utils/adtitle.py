from requirement import Requirement

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
