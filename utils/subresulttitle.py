from requirement import Requirement


class SubResultTitle(Requirement):
	def __init__(self):
		self._nome = 'tituloSubresultados'
		self.data_flag = False
		self._dados = []
		self.lista = ["table",
                    "tr",
                    "td",
                    "div",
                    "span",
                    "h3",
                    "a",
                    "div",
                    "div",
                    "br"]
		self.estado = 0

	def shandletag(self, tagin, attrs):
		if tagin == self.lista[self.estado]:
			if self.estado == 6:
				self.data_flag = True
			self.estado += 1
			if self.estado >= len(self.lista):
				self.estado = 2
		else:
			self.estado = 0

	def ehandletag(self, tagin):
		if tagin == "tr" and self.estado > 0:
			self.estado = 1

	def shandledata(self, data):
		if self.data_flag:
			self._dados.append(data)
			self.data_flag = False
