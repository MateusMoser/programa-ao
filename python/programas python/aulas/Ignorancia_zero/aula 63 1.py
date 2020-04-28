class Banco(object):
    def __init__(self,total,taxareser,reservaexig):
        self.__total = total
        self.taxareserva = taxareser
        self.__reservaexigida = reservaexig


class Conta():
    def __init__(self,saldo,ID,senha):
        self.__saldo = saldo
        self.__ID = ID
        self.__senha = senha

    def deposito(self,senha,valor):
        if senha == self.__senha:
            self.__saldo += valor

    def saque(self,senha,valor):
        if senha == self.__senha:
            self.__saldo -= valor

    def emprestimo(self,valor):
        if self.__saldo > 0:
            print('pode')
        else:
            print('nao pode')
    def saldo(self):
        print(f'Voce possui {self.__saldo} R$')

marcos = Conta(4001,3141,'password')
marcos.deposito('password',1000)
marcos.saldo()
marcos.emprestimo(7000)