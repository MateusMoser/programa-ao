valor = float(input('qual o valor da casa?:'))
salario = float(input('qual seu salario?:'))
anos = int(input('em quantos anos voce quer pagar?:'))
meses = anos*12
valor2 = valor/meses
print ('voce vai pagar em {} meses'.format(meses))
print ('voce ira pagar {:.2f} por mes'.format(valor2))
if valor2 >= salario*0.30/100:
    print('emprestimo negado')
else:
    print ('emprestimo aceito')