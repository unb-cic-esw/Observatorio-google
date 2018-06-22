from requirement import Requirement

# Essa é uma classe abstrata que representa todos os requisitos que
# não são atômicos, isso é, requisitos que tem outros requisitos.
# Por exemplo: Ad representa os dados sobre resultados patrocinados
# Que por sua vez, é formado pelos dados de AdPreview, AdTitle e AdLink.
class CompositeRequirement(Requirement):
    def __init__(self):
        super(CompositeRequirement, self).__init__()
        self.lista = []

    def dados(self):
        for i in range(0, len(self.lista[0].dados())):
            acc = {}
            for req in self.lista:
                acc[req.nome()] = req.dados()[i]
            self._dados.append(acc)
        return self._dados

    def shandletag(self, tagin, attrs):
        for req in self.lista:
            req.shandletag(tagin, attrs)

    def ehandletag(self, tagin):
        for req in self.lista:
            req.ehandletag(tagin)

    def shandledata(self, data):
        for req in self.lista:
            req.shandledata(data)
