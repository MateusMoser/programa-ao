jogador = dict()
gols = []
totgol = 0
jogador['nome'] = str(input('Nome do jogador'))
jogador['jogos'] = int(input('Quantos jogos eles jogou?'))
for c in range(jogador['jogos']):
    gol = int(input(f'Quantos gols ele fez na {c+1}º partida?'))
    totgol += gol
    gols.append(gol)
jogador['gols'] = gols
print('=='*20)
for k,v in jogador.items():
    print(f'{k}={v}')
print(f'{jogador["nome"]} fez {totgol} gols, em {jogador["jogos"]} jogos.')
for i,v in enumerate(jogador['gols']):
    print(f' Na partida  {i+1}, fez {v} gols')