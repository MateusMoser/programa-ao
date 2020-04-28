alt = float (input('qual sua altura'))
peso = float(input('qual seu peso'))
imc = peso / (alt**2)
print ('seu IMC é de {:.2f} '.format(imc))
if imc <= 18.5:
    print ('voce esta abaixo do peso ideal')
elif imc <= 25:
    print (' voce esta no peso ideal')
elif imc <= 30:
    print('voce esta em fase de sobrepeso')
elif imc <= 40:
    print ('voce tem obesidade')
elif imc > 40:
    print ('voce tem obesidade morbida')