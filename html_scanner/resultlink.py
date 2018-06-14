from requirement import Requirement


# Essa classe representa o link de um resultado não patrocinado
class ResultLink(Requirement):
	def __init__(self):
		self._nome = 'linkResultados'
		self.h3flag = False
		self._dados = []
		self.srgflag = False
		self.scopecounter = 0

	def shandletag(self, tagin, attrs):
		if self.srgflag:
			self.scopecounter += 1
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
		else:
			if tagin == "div":
				for attr in attrs:
					if attr == ('class', 'srg'):
						self.srgflag = True

	def ehandletag(self, tagin):
		if self.srgflag:
			if self.scopecounter == 0:
				self.srgflag = False
			else:
				self.scopecounter -= 1

	def shandledata(self, data):
		return

	def checkflag(self):
		return
