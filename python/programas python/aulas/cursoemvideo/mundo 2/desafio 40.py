nota1 = float(input('digite a primeira nota do aluno'))
nota2 = float(input('digite a segunda nota do aluno'))
media = (nota1+nota2)/2
if media < 5.0:
    print ('aluno reprovado')
elif media >= 7:
    print ('aluno aprovado')
elif 7 > media >= 5:
    print('aluno de recuperaçao')