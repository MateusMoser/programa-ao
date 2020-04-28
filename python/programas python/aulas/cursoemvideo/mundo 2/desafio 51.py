termo1 = int(input('primeiro termo'))
razao = int(input('razao'))
decimo = termo1 + (10-1) * razao
for c in range (termo1,decimo,razao):
    print ('{}'.format(c),end='=')
print('fim')

#Desenvolva um programa que leia o primeiro termo e a razão
# de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.