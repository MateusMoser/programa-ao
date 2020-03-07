from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10),
     randint(1,10), randint(1,10), )
print ('Os valores sorteados sao: ',end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print('\nO maior valor foi ', max(numeros))
print('O menor valor foi ',min(numeros))