termo1 = int(input('primeiro termo'))
razao = int(input('razao'))
termo = termo1
cont = 1
quant = 10
while cont <= quant:
    print('{}'.format(termo), end=' ')
    termo += razao
    cont += 1
    print('quantos termos queres mostrar a mais')
