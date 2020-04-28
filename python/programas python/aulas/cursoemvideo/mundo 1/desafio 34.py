sal = float(input('digite seu salario'))
if sal >= 1250:
    print('seu novo salario é {}'.format(sal*0.10+sal))
if sal <= 1250:
    print('seu novo salario é {}'.format(sal*0.15+sal))