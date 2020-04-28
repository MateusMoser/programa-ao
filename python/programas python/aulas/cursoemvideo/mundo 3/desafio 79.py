list = []
while True:
    num = int(input('Digite um valor'))
    if num not in list:
        list.append(num)
    cont = str(input('Voce deseja continuar [S/N]')).upper()
    if cont == 'N':
        break
print(sorted(list))
