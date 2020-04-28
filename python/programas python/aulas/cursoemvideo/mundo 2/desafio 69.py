idade = 0
sexo = 0
quantidade = 0
quantsexo = 0
mulher20 = 0
while True:
    idade = int(input('Digite uma idade '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F] ')).strip().upper()
    if idade > 18:
        quantidade += 1
    if sexo == 'M':
        quantsexo += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Voce deseja continuar? [S/N]')).upper().strip()
    if cont == 'N':
        break
print (f'quantidade de homens com mais de 18 {quantidade}')
print (f'quantidade de homens {quantsexo}')
print (f'quantidade de mulheres com menos de 20 {mulher20}')
