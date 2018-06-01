from requirement import Requirement


class ResultLink(Requirement):
	def __init__(self):
		self._nome = 'linkResultados'
		self.h3flag = False
		self._dados = []

	def shandletag(self, tagin, attrs):
		if self.h3flag:
			if tagin == 'a':
				if attrs[0][0] == 'href':
					self._dados.append(attrs[0][1])
			self.h3flag = False
		else:
			if tagin == 'h3':
				for attr in attrs:
					if attr == ('class', 'r'):
						self.h3flag = True

	def ehandletag(self, tagin):
		return

	def shandledata(self, data):
		return

	def checkflag(self):
		return
