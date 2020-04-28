km = int(input('qual a velocidade '))
multa = (km-80)*7
if km >= 80:
    print('sua multa é de {}'.format(multa))
else:
    print('sem multas para voce hoje')