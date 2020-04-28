dado = 0
all = [[],[]]
for c in range(0,7):
    dado = int(input(f'digite p {c+1}º valor'))
    all.append(dado)
    if dado % 2 == 0:
        all[0].append(dado)
    elif dado % 2 != 0:
        all[1].append(dado)
all[0].sort() and all[1].sort()
print(f'Os valores impares foram {all[1]}')
print(f'Os valores pares foram {all[0]}')
