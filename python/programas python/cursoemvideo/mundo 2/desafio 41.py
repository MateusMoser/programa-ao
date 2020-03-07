from datetime import date
nascimento = int(input('ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - nascimento
print ('o atleta tem {} anos'.format(idade))
if idade <= 9:
    print('atleta mirim')
elif idade <= 14:
    print ('atleta infantil')
elif idade <= 19:
    print('atleta junior')
elif idade <= 25:
    print ('atleta senior')
elif idade > 25:
    print ('atleta master')
