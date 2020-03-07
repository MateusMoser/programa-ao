class Mamifero():
     def __init__(self,pelo,andar,sexo):
         self.pelo = pelo
         self.sexo = sexo
         self.andar = andar
     def falar(self):
         print('ola eu estou falando')
     def caminhar(self):
         print(f'tenho {self.andar} pernas e estou andando')
     def nadar(self):
        print('estou nadando')

class Pessoa(Mamifero):
     def __init__(self, pelo, andar, sexo,cabelo):
         super().__init__(pelo, andar, sexo)
         self.cabelo = cabelo

rex = Mamifero('preto',4,'m')
julia = Pessoa('preto',2,'f','loiro')
