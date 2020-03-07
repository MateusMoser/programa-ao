import random
n1 = random.randint(1,5)
n2 = int(input('digite um numero de um a 5 '))
if n1==n2:
    print('parabens voce acertou')
else:
    print ('voce nao sabe qual numero o computador pensou')
    print('o numero era {}'.format(n1))