from compositerequirement import CompositeRequirement
from subresulttitle import SubResultTitle
from subresultlink import SubResultLink

# Essa classe representa os dados de um subresultado
class SubResult(CompositeRequirement):
    def __init__(self):
        self._nome = 'SubResultado'
        self._dados = []
        self.lista = []
        self.lista.append(SubResultTitle())
        self.lista.append(SubResultLink())
