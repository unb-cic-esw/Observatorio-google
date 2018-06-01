from requirement import Requirement

class TopStoryTitle(Requirement):
	def __init__(self):
		self.tags = set()
		self.tags.add('div')
		self._nome = 'tituloNoticias'
		self.flag = False
		self.atributos = set()
		self.atributos.add(('style', '-webkit-line-clamp:4;height:5.5em'))
		self._dados = []

	def shandletag(self, tagin, attrs):
		if tagin in self.tags:
			aux = [tagin]
			for attr in attrs:
				if attr in self.atributos:
					aux += [attr]
			if len(aux) > 1:
				self.flag = True

	def ehandletag(self, tagin):
		return

	def shandledata(self, data):
		if self.checkflag():
			self._dados.append(data)

	def checkflag(self):
		if self.flag:
			self.flag = False
			return True
		else:
			return self.flag
