class Mamifero(object):
    def __init__(self, pelo, vida, filhos):
        self.pelo = pelo
        self.vida = vida
        self.filhos = filhos


class Pessoa(Mamifero):
    def __init__(self, nome, cabelo, olho, pele, pelo, vida, filhos):
        super().__init__(pelo, vida, filhos)
        self.nome = nome
        self.cabelo = cabelo
        self.olho = olho
        self.pele = pele

    def andar(self):
        print(f'{self.nome} e estou andando')

    def nadar(self):
        print('estou nadando')


millena = Pessoa('Millena', 'loiro', 'azul', 'clara', 'claro', 80, 2)
millena.andar()
print(millena.nome)
