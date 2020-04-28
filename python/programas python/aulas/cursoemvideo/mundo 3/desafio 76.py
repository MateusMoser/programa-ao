lista = ('lapis',1.50,
         'borracha',2,
         'sabonete',3.40,
         'casaco',79.90,
         'gravata',50.50)
print('='*10 ,'LISTAGEM DE PREÇOS', '='*10)
for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print (f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R${lista[pos]:>7.2f}')