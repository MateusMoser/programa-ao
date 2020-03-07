somaidade = 0
media = 0
maiorhomem = 0
nomevelho = 0
mulher20 = 0
for p in range (1,5):
    print ('====== {}º PESSOA ======'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        mulher20 += 1
media = somaidade / 4
print ('A media de idade do grupo é de {} anos'.format(media))
print ('O homem mais velho tem {} anos e se chama {}.'.format(maiorhomem,nomevelho))
print ('Ao todo sao {} mulheres com meno de 20 anos'.format(mulher20))