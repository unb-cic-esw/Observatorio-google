from requirement import Requirement


# Essa classe representa o link de um subresultado
class SubResultLink(Requirement):
	def __init__(self):
		self._nome = 'linkSubresultados'
		self._dados = []
		self.lista = [
                    'table',
              						'tr',
              						'td',
              						'div',
              						'span',
              						'h3',
              						'a',
              						'div',
              						'div',
              						'br']
		self.estado = 0

	def shandletag(self, tagin, attrs):
		if tagin == self.lista[self.estado]:
			if self.estado == 6:
				self._dados.append(attrs[1][1])
			self.estado += 1
			if self.estado >= len(self.lista):
				self.estado = 2
		else:
			self.estado = 0

	def ehandletag(self, tagin):
		if tagin == "tr" and self.estado > 0:
			self.estado = 1

	def shandledata(self, data):
		pass
