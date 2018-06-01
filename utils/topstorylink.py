from requirement import Requirement

class TopStoryLink(Requirement):
	def __init__(self):
		self.tags = set()
		self.tags.add('g-inner-card')
		self._nome = 'linkNoticias'
		self.gflag = False
		self._dados = []

	def shandletag(self, tagin, attrs):
		if self.gflag:
			if tagin == 'a':
				self._dados.append(attrs[0][1])
			self.gflag = False
		elif tagin in self.tags:
			self.gflag = True

	def ehandletag(self, tagin):
		return

	def shandledata(self, data):
		return
