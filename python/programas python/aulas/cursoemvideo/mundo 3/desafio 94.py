#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas                   B) A média de idade            C) Uma lista com as mulheres             D) Uma lista de pessoas com idade acima da média
##declaraçao de variaveis
pessoa = {}
list = []
mulheres = []
velhos = []
totidade = 0
#input de dados
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = str(input('Sexo [ M/F]: ')).upper()
    list.append(pessoa)
    totidade += pessoa['idade']
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    while pessoa['sexo'] not in 'MmFf':
        print('Apenas [M/F]')
        sexo = str(input('Sexo [ M/F]: ')).upper()
    cont = str(input('Deseja continuar? [S/N]?')).upper()
    while cont not in 'SsNn':
        cont = str(input('Deseja continuar? [S/N]?')).upper()
    if cont == 'N':
        break
medida = totidade/len(list)
print(f'O total de pessoas cadastradas foi de {len(list)}')
print(f'A media de idade das pessoas é de {medida}')
print(f'As mulheres cadastradas foram: {mulheres}')
print('a lista de pessoas mais velhas do que a media é:')
for p in list:
    if p['idade'] >= medida:
        print('___'*20)
        for k,v in p.items():
            print(f'{k} = {v}; ',end=' ')

