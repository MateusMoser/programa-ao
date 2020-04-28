n = 0
s = 0
cont = 0
while True:
    n = int(input('Digite um valor'))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma foi {s}')
print('A quantidade de numeros foi',cont)
