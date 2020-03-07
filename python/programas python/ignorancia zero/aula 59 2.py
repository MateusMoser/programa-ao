"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e
calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe
as medidades de um local. Depois, deve criar um objeto com as medidas e calcular
a quantidade de pisos necessárias para o local.
"""


class Retangulo:
    def __init__(self):
        self.base = 0
        self.altura = 0

    def mudavalor(self, b, a):
        self.base = b
        self.altura = a

    def retorna(self):
        return self.altura and self.base

    def calcarea(self):
        return self.base * self.altura

    def calcper(self):
        return 2 * (self.base + self.altura)

largura = float(input('Digite a altura'))
comprimento = float(input('Digite o comprimento'))

piso = Retangulo()

lagpiso = float(input('Digite a altura'))
compiso = float(input('Digite o comprimento'))

piso.mudavalor(lagpiso,compiso)

area = largura*comprimento
numpsiso = round(area/piso.calcarea())

print(f'Sera necessarios {numpsiso}')