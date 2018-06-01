from requirement import Requirement

class ResultPreview(Requirement):
	def __init__(self):
		self._nome = 'previsaoResultados'
		self.h3flag = False
		self.data_flag = False
		self._dados = []
		self.dado = ""
		self.spans_aninhados = 0

	def shandletag(self, tagin, attrs):
		if tagin == 'span' and ('class', 'st') in attrs:
			if self.spans_aninhados == 0:
				self.spans_aninhados += 1
				self.data_flag = True
		elif tagin == 'span' and self.data_flag:
			self.spans_aninhados += 1

	def ehandletag(self, tagin):
		if tagin == 'span' and self.data_flag:
			self.spans_aninhados -= 1
			if self.spans_aninhados == 0:
				self._dados.append(self.dado.strip())
				self.dado = ''
				self.data_flag = False

	def shandledata(self, data):
		if self.data_flag:
			self.dado += data
