jogadores = {}
elenco_clube = []
gol_partidas = []

total_gol = 0

while True:
    print('==' * 20)
    jogadores.clear()
    gol_partidas.clear()

    jogadores['nome'] = str(input('Nome do jogador: ')).title()

    quant_partida = int(input(f'Número de partidas do jogador {jogadores["nome"]}: '))
    for i in range(quant_partida):
        gol_partidas.append(int(input(f'Partida {i}: ')))
        total_gol = sum(gol_partidas)

    jogadores['gol'] = gol_partidas[:]
    jogadores['total'] = total_gol
    elenco_clube.append(jogadores.copy())

    pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while pergunta not in 'SnNn':
        pergunta = str(input('Resposta inválida!\nQuer continuar? [S/N]: ')).strip().upper()[0]
    if pergunta in 'Nn':
        break

print('==' * 20)
print('cod ', end='')
for key in jogadores.keys():
    print(f'{key:<13}', end='')
print()
print('--' * 20)

for chave, jogador in enumerate(elenco_clube):
    print(f'{chave:>3} ', end='')
    for j in jogador.values():
        print(f'{str(j):<13}', end='')
    print()

while True:
    print('==' * 20)

    opcao = int(input('Mostrar dados de qual jogador? '))
    if opcao == 999:
        break
    elif opcao < 0 or opcao > (len(elenco_clube) - 1):
        print(f'Erro! Não existe jogador com código {opcao}! Tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {elenco_clube[opcao]["nome"]}')
        for posicao, gol in enumerate(elenco_clube):
            if opcao == posicao:
                for indice, l in enumerate(elenco_clube[posicao]['gol']):
                    print(f'\tNo jogo {indice} fez {l} gols.')