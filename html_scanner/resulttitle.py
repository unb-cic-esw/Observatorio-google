from requirement import Requirement

# Essa classe representa o titulo de um resultado não patrocinado
class ResultTitle(Requirement):
    def __init__(self):
        self._nome = 'tituloResultados'
        self._dados = []
        self.h3flag = False
        self.dflag = False
        self.srgflag = False
        self.scopecounter = 0

    def shandletag(self, tagin, attrs):
        if self.srgflag:
            self.scopecounter += 1
            if self.h3flag:
                if tagin == 'a':
                    if attrs[0][0] == 'href':
                        self.dflag = True
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
        if self.dflag:
            self._dados.append(data)
            self.dflag = False

    def checkflag(self):
        return
