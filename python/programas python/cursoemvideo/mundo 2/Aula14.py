s = str(input('Digite seu sexo: ')).upper()
while s != 'M' and s != 'F' and s != 'TRENZINHO':
    print('Digite um sexo valido [M/F]')
    s = str(input('Digite o Seu Sexo: ')).upper()
if s == 'F':
    print ('proibida entrada de mulheres aqui')
elif s == 'M':
    print(' seja bem vindo')
elif s == 'TRENZINHO':
    print ('PIUIII')


