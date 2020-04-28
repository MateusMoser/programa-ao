sexo = str(input('Qual o seu sexo [M/F]? ')).upper().strip()

while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Por favor, digite novamente: ')).upper().strip()[0]
if sexo == 'M':
    print(f'FIM.\nSeu sexo é Masculino.')
else:
    print(f'FIM.\nSeu sexo é Feminino.')