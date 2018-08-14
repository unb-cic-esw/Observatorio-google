from requirement import Requirement


class VideoDescription(Requirement):
    def __init__(self):
        self._nome = 'linkVideos'
        self._dados = []
        self.lista = ['div',
                      'div',
                      'div',
                      'h3',
                      'a'
                      ]
        self.estado = 0
        self._flag = False

    def shandletag(self, tagin, attrs):
        if self.estado == 0 and ('class', 'g') in attrs and tagin == self.lista[0]:
            self.estado += 1
        elif self.lista[self.estado] == tagin:
            self.estado += 1
        if self.estado == 5:
            self._flag = True
            self.estado = 0

    def ehandletag(self, tagin):
        pass

    def shandledata(self, data):
        if self._flag:
            self._dados.append(data)
            self._flag = False
