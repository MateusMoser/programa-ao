import random
n1 = 0
n2 = 0
s = 0
res = 0
vit = 0
while True:
    n1 = random.randint(1, 10)
    n2 = int(input('Digite um valor para jogar par ou impar'))
    esc = ' '
    while esc not in 'PI':
        esc = str(input('Par ou impar? [P/I]')).strip().upper()[0]
    s = n1 + n2
    res = s % 2
    if res != 0:
        if esc == 'I':
            print ('Voce ganhou')
            vit += 1
        if esc == 'P':
            print('VOCE PERDEU')
        break
    if res == 0:
        if esc == 'P':
            print('Voce ganhou')
            vit += 1
        if esc == 'I':
            print('Voce perdeu')
print('a soma deu',s)
print('voce obteve {} vitorias consecutivas'.format(vit))
print(res)