from requirement import Requirement

# Essa classe representa o texto de um resultado patrocinado
class AdPreview(Requirement):
    def __init__(self):
        self._nome = 'previsaoPropagandas'
        self._dados = []
        self.dado = ""
        self.trigger = "div"
        self.outer_flag = False
        self.data_flag = False

    def check_trigger(self, attrs):
        for attr in attrs:
            if attr[0] == 'class' and 'ads-creative' in attr[1]:
                return True
        return False

    def shandletag(self, tagin, attrs):
        if not self.outer_flag:

            if tagin == self.trigger and self.check_trigger(attrs):
                self.outer_flag = True
                self.data_flag = True
        elif tagin == 'div' and ('class', 'ellip') in attrs:
            self.data_flag = True
        elif not self.data_flag:
            self.outer_flag = False
            self._dados.append(self.dado)
            self.dado = ""

    def ehandletag(self, tagin):
        if tagin == "div" and self.data_flag:
            self.data_flag = False

    def shandledata(self, data):
        if self.data_flag:
            self.dado += data + ""
