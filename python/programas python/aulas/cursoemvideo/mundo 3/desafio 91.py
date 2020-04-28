from random import randint
from operator import itemgetter
jogo = {}
for c in range(0,4):
    jogo[f'jogador {c+1}'] = randint(0,6)
rank = {}
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado')
rank = sorted(jogo.items(),key=itemgetter(1), reverse=True)
for i,v in enumerate(rank):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')