estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Digite o estado'))
    estado['sigla'] = str(input('Digite a sigla'))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()