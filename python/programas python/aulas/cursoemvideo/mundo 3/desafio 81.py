lista = []
quant = 0
while True:
    num = int(input('Digite um valor'))
    lista.append(num)
    quant += 1
    cont = str(input('Deseja continuar:[S/N]? ')).upper()
    if cont == 'N':
        break
print (f'Voce digitou {quant} elementos')
print (f'A ordem decrescente dos elementos sao {lista.reverse()}')
if quant < 5:
    print('O quinto valor nao foi encontrado na lista')
else:
    print(f'O quinto valor é {lista.index(5)}')