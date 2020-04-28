total = totmil = menor = cont =0
barato = ' '
while True:
    prod = str(input('Digite o nome do produto'))
    prec = float(input('Digite o valor do produto: R$ '))
    total += prec
    cont =+ 1
    if prec > 1000:
        totmil += 1
    if cont == 1 or prec < menor:
        menor = prec
        barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('QUER CONTINUAR S/N')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de {total:.2f}')
print(f'Temos {totmil} produtos custando mais de mil reais')
print(f'O produto mais é {barato} e barato custa {menor}')