from datetime import date
ano = int(input('qual o ano que deseja analisar?digite zero se deseja o ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400:
    print('o ano {} é BISSEXTO'.format(ano))
else:
    print('o ano {} NAO é BISSEXTO'.format(ano))
