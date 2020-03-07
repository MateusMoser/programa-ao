km= float(input('qual a kilometragem da viagem? '))
if km <= 200:
    print('sua viagem custara {}'.format(km*0.50))
else:
    print('sua viagem custara {}'.format(km*0.45))