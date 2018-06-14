# Essa classe representa um requisito atômico, isto é,
# um requisito que não depende de outros requisitos.
class Requirement():

	def __init__(self):
		self._dados = None
		self._nome = None

	def dados(self):
		return self._dados

	def nome(self):
		return self._nome
