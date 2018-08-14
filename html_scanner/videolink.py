from requirement import Requirement


class VideoLink(Requirement):
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

    def shandletag(self, tagin, attrs):
        if self.estado == 0 and ('class','g')  in attrs and tagin == self.lista[0]:
            self.estado += 1
        elif self.lista[self.estado] == tagin:
            self.estado += 1
        if self.estado == 5:
            self._dados.append(attrs[0][1])
            self.estado = 0


    def ehandletag(self, tagin):
        pass

    def shandledata(self, data):
        pass
