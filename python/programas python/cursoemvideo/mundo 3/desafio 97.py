def escreva(txt):
    tam = len(txt) + 4
    print('='*tam)
    print(f'  {txt}')
    print('='*tam)

escreva(str(input('Digite o texto')))