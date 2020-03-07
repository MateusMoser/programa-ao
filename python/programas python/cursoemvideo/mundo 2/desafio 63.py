quant = int(input('Digite a quantidade de termos que voce deseja'))
n1 = 0
n2 = 1
cont = 3
n3 = 0
print ('{} = {}'.format(n1,n2), end= ' ')
while cont <= quant:
    n3 = n1 + n2
    print('=',n3,end=' ')
    n1 = n2
    n2 = n3
    cont += 1