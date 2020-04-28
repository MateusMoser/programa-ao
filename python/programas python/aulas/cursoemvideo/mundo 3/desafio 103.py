def ficha(nome='-naoinformado-',gols='-naoinformado-'):
    if nome == '':
        nome = 'naoinformado'
    if gols == '':
        gols = 'naoinformado'
    print(f'O nome do jogador é {nome} e a quantidade de gols é {gols}')


ficha(str(input('Digite o nome')).strip()
          ,str(input('Digite quantos gols')).strip())
