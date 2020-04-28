ns = tuple(int(input('Digite o {}º numero: '.format(i+1))) for i in range(4))
print('Voce digitou os valores ',ns)
print(f'O valor 9 apareceu {ns.count(9)}')
if 3 in ns:
    print(f'O valor 3 foi digitado primeiramente na {ns.index(3)+1}º posiçao')
else:
    print('O valor 3 nao foi digitado')
print('Os valores pares digitados foram')
for n in ns:
    if n % 2 == 0:
        print(n, end=' ')

