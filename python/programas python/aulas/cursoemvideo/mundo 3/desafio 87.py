#variaveis e listas
matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0

#fornecimento de dados
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input((f'Digit eum valor para [{l},{c}]')))
#mostrando os dados
for l in range(0,3):
     for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
     print()
for c in range(0,3):
    scol += matriz[c][2]

print('x'*60)
print(f'A soma dos pares é {spar}')
print(f'A soma dos valores da terceira coluna é {scol}')
print(f'O maior numero da segunda linha é {max(matriz[1])}')
