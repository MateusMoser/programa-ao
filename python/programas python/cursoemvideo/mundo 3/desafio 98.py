def contador(inicio,fim,passo):
    print(f'contade de {inicio} até o {fim} pulando {passo}')
    cont = inicio
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio<fim:
        while cont <= fim:
            print(cont,end=' ')
            cont += passo
    else:
        while cont >= fim:
            print(cont,end=' ')
            cont -= passo
    print()

contador(1,10,1)
contador(10,1,2)
contador(int(input('Inicio')),
         int(input('fim')),
         int(input('Passo')))