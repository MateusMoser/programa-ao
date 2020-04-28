from random import randint
def maior(*num):
    print(f'Os valores informados foram: {num}')
    print(f'Um total de {len(num)} valores')
    mai = men = max(num)
    for n in num:
        if n == 0:
            mai = n
            men = n
        if n > mai:
            mai = n
        if n < men:
            men = n
    print(f'O maior numero deles é {mai} e o menor numero é {men}')


#while True:
#    num = int(input('Digite um valor'))
#    nums.append(num)
#    cont = str(input('Deseja continuar [s/n]')).upper()
#    if cont == 'N':
#        break
maior(randint(1,100),randint(1,100),randint(1,100))