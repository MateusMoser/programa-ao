galera = []
dado = list()
#rececendo os dados
for c in range(0,3):
    dado.append(str(input('Nome')))
    dado.append(int(input('idade')))
    galera.append(dado[:])
    #apagando os dados depois de adicionar na lista maior
    dado.clear()
print(galera)