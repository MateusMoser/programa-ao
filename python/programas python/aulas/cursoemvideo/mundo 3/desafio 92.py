#importando dados pra puxar ano atual
from datetime import datetime
anoatual = datetime.now().year
#recebendo os dados no dicionario
dic = {}
dic['nome'] = str(input('Digite o nome'))
dic['nasc'] = int(input('Digite o ano de nascimento'))
idade = anoatual - dic['nasc']
dic['idade'] = idade
dic['CTPS'] = int(input('Digite o CTPS (0 se nao tiver)'))
#se o ctps for diferente de 0 pedir salario e ano de contrataçao
if dic['CTPS'] > 0:
    dic['Contratacao'] = int(input('Ano de contrataçao'))
    dic['Salario'] = float(input('Qual o seu salario'))
    # calculos
    dic['aposentadoria'] = dic['Contratacao'] + 35
    #mostrando os dados
    for k,v in dic.items():
        print(f'{k}={v}')
else:
    print('dai tu me complica parceiro')