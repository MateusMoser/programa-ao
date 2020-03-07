quant = int(input('Quantos reais voce deseja retirar?: '))
n1 = n50 = n30 = n4 = n5 = n6 = n7 = 0
while True:
    if quant >= 100:
        n1 += 1
        quant -= 100
    elif quant >= 50:
        n50 += 1
        quant -= 50
    elif quant >= 20:
        n30 += 1
        quant -= 20
    elif quant >= 10:
        n4 += 1
        quant -= 10
    elif quant >= 5:
        n5 += 1
        quant -= 5
    elif quant >= 2:
        n6 += 1
        quant -= 2
    elif quant == 1:
        n7 += 1
        quant -= 1
    if quant == 0:
        break
print(f'Voce recebeu')
if n1 > 0:
    print(f'{n1} notas de 100 ')
if n50> 0:
    print(f'{n50} notas de 50 ')
if n30>0:
    print(f'{n30} notas de 20 ')
if n4 > 0:
    print(f'{n4} notas de 10 ')
if n5 >0:
    print(f'{n5} notas de 5 ')
if n6 > 0:
    print(f'{n6} notas de 2 ')
if n7 > 0:
    print(f'{n7} nota de 1')
