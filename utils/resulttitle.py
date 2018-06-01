from requirement import Requirement

class ResultTitle(Requirement):
	def __init__(self):
		self._nome = 'tituloResultados'
		self._dados = []
		self.h3flag = False
		self.dflag = False

	def shandletag(self, tagin, attrs):
		if self.h3flag:
			if tagin == 'a':
				if attrs[0][0] == 'href':
					self.dflag = True
			self.h3flag = False
		else:
			if tagin == 'h3':
				for attr in attrs:
					if attr == ('class', 'r'):
						self.h3flag = True
					

	def ehandletag(self, tagin):
		return

	def shandledata(self, data):
		if self.dflag:
			self._dados.append(data)
			self.dflag = False

	def checkflag(self):
		return
