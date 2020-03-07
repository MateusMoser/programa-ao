def leiaint():
    n = input('Digite um valor inteiro')
    n.isalnum()
    while True:
        if n.isdecimal() == True:
            print(f'{n} é um numero inteiro')
        else:
            print(f'"{n}" nao é um numero inteiro')
        break
    return


repost = leiaint()