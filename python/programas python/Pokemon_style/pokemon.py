from random import randint


class Item():
    def __init__(self,name,tipo,stamina,health):
        #tipos [Potion,Weapon,Armor]
        self.name = name
        self.tipo = ''
        self.stam_regen = stamina
        self.health_regen = health


class Monster():
    def __init__(self,name,life,damage,magic,stamina):
        self.mname = name
        self.life = life
        self.damage = damage
        self.magic = magic
        self.stamina = stamina
        self.inventory = []

    def punch(self,other):
        if self.stamina > 5:
            self.hit = self.damage + randint(1,5)
            other.life -= self.hit
            print(f'{self.mname} socou e causou {self.hit} de dano')
            self.stamina -= 5
        else:
            print('estamina insuficiente')

    def super(self,other): 
        pass

    def magic_hit(self,other):
        if self.stamina > 15:
            self.hit = self.magic + randint(3,10)
            other.life -= self.hit
            self.stamina -= 15
            print(f'{self.mname} deu dano magico e causou {self.hit} de dano')
        else:
            print('estamina insuficiente')

    def use_item(self,item):
        self.life += item.health_regen
        self.stamina += item.stam_regen

    def add_item(self,item):
        self.inventory.append(item)

    def show_inventory(self):
        print('seu inventario contem;')
        self.counter = 0
        for item in self.inventory:
            print(f'[{self.counter}] {item.name}')
            self.counter += 1
        print(f'[{self.counter}]voltar')
        print('deseja usar algum item?')
        self.pick = int(input('+'))

        if self.pick == self.counter:
            #player 1 status
            print('='*20)
            print(f'nome = {self.mname}\nvida = {self.life}\nstamina = {self.stamina}')
            print('='*20)
            #Açao do player1
            print(f'escolha uma açao \n[1]soco 5 stami3na \n[2]ataque magico 15 stamina\n[3]Mostrar inventario')
            return

        elif self.pick >= 0 < self.counter:
            self.use_item(self.inventory[int(self.pick)])
            return


class Arena():
    def __init__(self,monster1,monster2):
        self.monsters = [monster1,monster2]
        self.monster1 = monster1
        self.monster2 = monster2
        
    def fight(self):
        self.rounder = 10
        while True:
            if self.rounder % 2 == 0:
                self.monster = self.monsters[0]
                self.enemy = self.monsters[1]
            else:
                self.monster = self.monsters[1]
                self.enemy = self.monsters[0]
            
            
            #player status
            print('='*20)
            print(f'nome = {self.monster.mname}\nvida = {self.monster.life}\nstamina = {self.monster.stamina}')
            print('='*20)
            #Açao do player
            print(f'escolha uma açao \n[1]soco 5 stamina \n[2]ataque magico 15 stamina\n[3]Mostrar inventario')
            while True:
                self.pick = int(input('='*20))
                if self.pick == 1:
                    self.monster.punch(self.enemy)
                    break
                elif self.pick == 2:
                    self.monster.magic_hit(self.enemy)
                    break
                elif self.pick == 3:
                    self.status_check = self.monster.life + self.monster.stamina
                    self.monster1.show_inventory()
                    self.status_check2 = self.monster.life + self.monster.stamina
                    if self.status_check2 == self.status_check:
                        break
                    else:
                        break
                else:
                    self.pick = int(input('Digite apenas 1 ou 2'))
                
                self.rounder += 1
                
     
            
#criando os monstros
buzz = Monster('Millena',100,7,11,50)
krok = Monster('Mateus',100,5,13,50)

#criando os itens
mana_p = Item('mana potion','potion',15,0)
health_p = Item('healht potion','potion',0,15)

#adicionando os items nos monstros
buzz.add_item(mana_p)
buzz.add_item(health_p)
krok.add_item(mana_p)
krok.add_item(health_p)

#    MAIN   #
casa = Arena(buzz,krok)
casa.fight()
