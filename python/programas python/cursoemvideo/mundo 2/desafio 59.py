n1 = int(input('Digite um valor'))
n2 = int(input('digite um valor'))
op = 0
while op != 5 :

    print('''oque voce deseja fazer
    [1] somar
    [2] multiplicar
    [3] Maior
    [4] novos numeros
    [5]sair do programa''')
    op = int(input(''))
    if op == 1:
        soma = n1+n2
        print('A soma dos valores é igual a {}'.format(soma))
    elif op == 2:
        multi = n1*n2
        print('A multiplicaçao dos valores é',multi)
    elif op == 3:
        if n1>n2:
            print ('{} é maior que {}'.format(n1,n2))
        else:
            print('{} é maior que {}'.format(n2,n1))
    elif op == 4:
        print('Informe os valores novamente')
        n1 = int(input('Digite um valor'))
        n2 = int(input('digite um valor'))
    elif op == 5:
        print('========'*15)
        print('FIM DO PROGRAMA')
        print('========' * 15)
    else:
        print('digite um numero valido')