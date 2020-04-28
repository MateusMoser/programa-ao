import random
n1 = random.randint(1,10)
n2 = int(input('digite um numero de 1 a 10 '))
n3 = 1
if n2 > 10:
    print('digite um valor de 1 a 10')
while n1 != n2:
    n2 = int(input('Digite novamente'))
    n3 = n3 + 1
if n1==n2:
    print('parabens voce acertou')
    print('e foram necessarios {} tentativas'.format(n3))
