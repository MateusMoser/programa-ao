import random
from time import sleep

class Lutador():
    def __init__(self,vida,nome):
        self.vida = vida
        self.nome = nome

    def socar(self,other):
        dano = random.randint(1,5)
        other.vida -= dano
        print(f'{self.nome} socou {other.nome} e causou {dano} de dano')
        print(f'{other.nome} esta com {other.vida} de vida')
        return other.vida

class Luta():
    def __init__(self,lutador1,lutador2):
        self.lutador1 = lutador1
        self.lutador2 = lutador2

    def perdedor(self):
        if self.lutador1.vida < self.lutador2.vida:
            return self.lutador1
        return self.lutador2

    def ganhardor(self):
        if self.lutador1.vida > self.lutador2.vida:
            return self.lutador1
        return self.lutador2

    def batalha(self):
        lista = [self.lutador2,self.lutador1]
        a = random.choice(lista)
        while True:
            b = random.choice(lista)
            if b == a:
                b = random.choice(lista)
            else:
                break
        while True:
            a.socar(b)
            sleep(1)
#            print(f'{a.nome} socou {b.nome}')
            b.socar(a)
            sleep(1)
#            print(f'{a.nome} socou {b.nome}')

            if a.vida <= 0:
                print(f'O lutador {b.nome} foi o vencedor')
                break
            elif b.vida <= 0:
                print(f'O lutador {a.nome} foi o vencedor')
                break

joao = Lutador(30,'joao')
jose = Lutador(30,'jose')
ufc = Luta(joao,jose)
ufc.batalha()