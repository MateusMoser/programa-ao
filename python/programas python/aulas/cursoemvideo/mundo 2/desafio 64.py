quantn = 0
soma = 0
num = int(input('Digite um valor'))
while num != 999:
    quantn += 1
    soma += num
    num = int(input('Digite um valor'))
    if num == 999:
        print ('Voce digitou {} valores e a soma deles deu {}'.format(quantn,soma))