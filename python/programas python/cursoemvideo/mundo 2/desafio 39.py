import datetime
ano = datetime.date.today().year
nasc = int(input('digite seu ano de nascimento'))
dif = ano-nasc
if dif == 18:
    print(' voce precisa se alistar imediatamente')
elif dif > 18:
    saldo = dif - 18
    print ('voce ja devia ter se alistado')
    print('voce devia ter se alistado ha {} anos'.format(saldo))
elif dif < 18:
    saldo = 18 - dif
    print ('voce ainda precisa se alistar')
    print ('voce tera que se alistar em {} anos'.format(saldo))