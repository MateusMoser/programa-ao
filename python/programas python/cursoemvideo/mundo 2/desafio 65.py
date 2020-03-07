valor = int(input('digite um valor'))
cont = str(input('voce deseja continuar? [s/n]')).upper()
maior = menor = 0
quant = 1
soma = 0
while cont != 'N':
    valor  = int(input('digite outro valor'))
    soma += valor
    if quant == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    quant += 1
    cont = str(input('voce deseja continuar? [s/n]')).upper()
media = soma / quant
print ('Voce escreveu {} numeros'.format(quant))
print ('a media desses numeros foi {}'.format(media))
print ('O maior numero foi {} e o menor numero foi {}'.format(maior,menor))
