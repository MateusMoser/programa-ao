class Ponto:
    def __init__(self):
        self.x = 0
        self.y = 0
    def imprimir_ponto(self):
        print(f'O valor x = {self.x} ')
        print(f'O valor y = {self.y}')

class Retangulo:
    def __init__(self):
        self.largura = 0
        self.altura = 0
        self.vertice = 0
    def centro_retangulo(self):
        x = self.largura/2 + self.vertice
        y = self.altura/2 + self.vertice

