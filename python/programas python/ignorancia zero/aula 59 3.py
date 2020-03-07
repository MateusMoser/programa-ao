"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor
que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa():
    def __init__(self, nome: object, idade: object, peso: object, altura: object) -> object:
        self.idade = 0
        self.nome = ''
        self.peso = 0.0
        self.altura = 0.0

    def envelhecer(self,tempo):
        self.idade += tempo
        if self.idade < 21:
            self.altura *= tempo * 1.005
        return self.peso

    def engorda(self, peso, kilos):
        peso += kilos
        return self.peso

    def emagrece(self, peso):
        self.peso -= peso
        return self.peso

    def cresce(self, altura):
        self.altura += altura
        return self.altura


pessoa = Pessoa(0,0,0,0)

pessoa.nome = str(input('Digite seu nome: '))
pessoa.idade = int(input('Digite sua idade: '))
pessoa.peso = float(input('Digite seu peso, separado por ponto: '))
pessoa.altura = float(input('Digite sua altura, separado por ponto: '))

envelhece = int(input('Deseja envelhecer quantos anos: '))
print(f'Nova idade: {pessoa.envelhecer(envelhece)} anos')