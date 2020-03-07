ficha = []
while True:
    nome = str(input('nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('Quer continuar')).upper()
    if resp == 'N':
        break
print()
print(f'{"No.":<4}{"nome":<10}{"media":<8}')
print()
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')