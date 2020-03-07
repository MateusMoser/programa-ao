#criaçao de variaveis
pessoas = []
mai = men = 0
dado = []
#input dos dados
while True:
    dado.append(str(input('Digite o nome')))
    dado.append(int(input('Digite um peso')))
#analise de dados
    if len(pessoas) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        elif dado[1] < men:
            men = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    cont = str(input('Deseja continuar [S/N]')).upper()
    if cont == 'N':
        break
print (f'Ao todos, voce cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {mai} kilos', end=' ')
for p in pessoas:
    if p[1] == mai:
        print(p[0])
print(f'O menor peso foi de {men} kilos',end=' ')
for p in pessoas:
    if p[1] == men:
        print(p[0])

