import random
itens = ('pedra' , 'papel' , 'tesoura')
computador = random.randint(0,2)
print ('suas escolhas sao')
print ('''0 = pedra
1 = papel 
2 = tesoura''')
jogador = int(input('qual sua jogada?'))
print ('='*111)
print ('computador jogou {}'.format(itens[computador]))
print ('jogador jogou {}'.format(itens[jogador]))
print ('='*111)
if computador == 0:
    if jogador == 0:
        print ('empate')
    elif jogador == 1:
        print ('jogador vence')
    elif jogador == 2:
        print ('jogador perde')
    else:
        print('jogada invalida')
elif computador == 1:
    if jogador == 0:
        print ('jogador perde ')
    elif jogador == 1:
        print ('EMPATE')
    elif jogador == 2:
        print ('jogador vence')
    else:
        print('jogada invalida')
elif computador == 2:
    if jogador == 0:
        print ('jogador vence')
    elif jogador == 1:
        print ('jogador perde')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('jogada invalida')