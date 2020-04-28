lista = []
impar = []
par = []
while True:
    num = int(input('Digite um numero'))
    lista.append(num)
    cont = str(input('Deseja continuar [s/n]')).upper()
    if cont == 'N':
        break
for num in lista:
    if num % 2 == 0:
            par.append(num)
    elif num % 2 != 0:
            impar.append(num)
print(lista)
print(impar)
print(par)