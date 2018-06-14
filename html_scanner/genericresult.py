from compositerequirement import CompositeRequirement
from ad import Ad
from result import Result

# Essa clase representa um resultado que pode ser patrocinado ou não
class GenericResult(CompositeRequirement):

	def __init__(self):
		self._nome = 'Resultado'
		self._dados = []
		self.lista = []
		self.lista.append(Ad())
		self.lista.append(Result())

	def dados(self):
		for item in self.lista[0].dados():
			acc = item
			item["is_ad"] = True
			self._dados.append(acc)

		for item in self.lista[1].dados():
			acc = item
			item["is_ad"] = False
			self._dados.append(acc)
		return self._dados
