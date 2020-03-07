from random import randint
njogos = int(input('Quantos jogos sera sorteados'))
jogo = [0,0,0,0,0,0]

for n in range(0,njogos):
     for c in range(0,6):
         jogo[c] = randint(1,60)
         if jogo[c] in jogo:
             jogo[c] += 1
     print(jogo)