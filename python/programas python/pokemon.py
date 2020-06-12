from random import randint


class Monster():
    def __init__(self,name,life,damage,magic,stamina):
        self.mname = name
        self.life = life
        self.damage = damage
        self.magic = magic
        self.stamina = stamina


    def punch(self,other):
        if self.stamina > 5:
            self.hit = self.damage + randint(1,5)
            other.life -= self.hit
            print(f'{self.mname} socou e causou {self.hit} de dano')
            self.stamina -= 5
        else:
            print('estamina insuficiente')

    def magic_hit(self,other):
        if self.stamina > 15:
            self.hit = self.magic + randint(3,10)
            other.life -= self.hit
            self.stamina -= 15
            print(f'{self.mname} deu dano magico e causou {self.hit} de dano')
        else:
            print('estamina insuficiente')
    def stam_regen(self):
        self.stamina += randint(7,12)


class Arena():
    def __init__(self,monster1,monster2):
        self.monster1 = monster1
        self.monster2 = monster2
        
    def fight(self):
        while True:
            #player 1 status
            print('='*20)
            print(f'nome = {self.monster1.mname}\nvida = {self.monster1.life}\nstamina = {self.monster1.stamina}')
            print('='*20)
            #Açao do player1
            print(f'escolha uma açao \n[1]soco 5 stamina \n[2]ataque magico 15 stamina')
            print('='*20)
            while True:
                self.pick = int(input('='))
                if self.pick == 1:
                    self.monster1.punch(self.monster2)
                    break
                elif self.pick == 2:
                    self.monster1.magic_hit(self.monster2)
                    break
                else:
                    self.pick = int(input('Digite apenas 1 ou 2'))
            
            #status player 2
            print('='*20)
            print(f'nome = {self.monster2.mname}\nvida = {self.monster2.life}\nstamina = {self.monster2.stamina}')
            print('='*20)
            #Açao do player2
            print(f'escolha uma açao \n[1]soco 5 stamina \n[2]ataque magico 15 stamina')
            print('='*20)
            while True:
                self.pick = int(input('='))
                if self.pick == 1:
                    self.monster2.punch(self.monster1)
                    break
                elif self.pick == 2:
                    self.monster2.magic_hit(self.monster1)
                    break
                else:
                    self.pick = int(input('Digite apenas 1 ou 2'))
            if self.monster1.life < 1:
                print(f'{self.monster2.mname} foi o vencedor')
                break
            if self.monster2.life < 1:
                print(f'{self.monster1.mname} foi o vencedor')
                break


buzz = Monster('buzz',50,10,10,50)
krok = Monster('krok',50,4,15,50)


casa = Arena(buzz,krok)
casa.fight()
