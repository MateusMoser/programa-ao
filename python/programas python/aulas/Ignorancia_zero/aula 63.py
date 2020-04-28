class ObjetoGrafico(object):
    def __init__(self, cor_de_preenximento, preenxida, cor_de_contorno):
        self.cor_de_preenximento = cor_de_preenximento
        self.preenxida = preenxida
        self.cor_de_contorno = cor_de_contorno


class Retangulo(ObjetoGrafico):
    def __init__(self, base, altura, cor_de_preenximento, preenxida, cor_de_contorno):
        super().__init__(cor_de_preenximento, preenxida, cor_de_contorno)
        self.base = base
        self.altura = altura
    def area(self):
        pass

    def perimetro(self):
        pass
