lista = list()
dic = {'nome':' ','media':0}
dic['nome'] = str(input('Digite o nome'))
dic['media'] = float(input('Digite uma media'))
for c, v in dic.items():
    print(f'{c} é igual a {v}')
if dic['media'] < 7:
    print('REPROVADO')
else:
    print('Aprovado')