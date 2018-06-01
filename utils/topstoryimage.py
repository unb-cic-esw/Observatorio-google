from requirement import Requirement


class TopStoryImage(Requirement):

	def __init__(self):
		self._nome = 'PrincipaisNoticiasImagens'
		self._dados = []
		self.contador = -1
		self.lista = ['g-img', 'img']

	def shandletag(self, tagin, attrs):
		if self.contador == -1:
			if tagin == 'div' and len(attrs) > 0 and attrs[0] == ('class', 'KNcnob'):
				self.contador = 0
		elif tagin == self.lista[self.contador]:
			self.contador += 1
		else:
			self.contador = -1

		if self.contador == 2:
			self._dados.append(attrs[1][1])
			self.contador = -1

	def ehandletag(self, tagin):
		pass

	def shandledata(self, data):
		pass
