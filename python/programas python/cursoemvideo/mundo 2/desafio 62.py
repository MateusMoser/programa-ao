primeiro = int(input('digite o termo'))
razao = int(input('Digite a razao'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' ')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('quantos termos voce quer mostrar a mais'))
print('fim')