unidades = ['litro','kilo','unid','metro']
estoque = []
produtos = []
class Produto:
    #produto que fica salvo no estoque, nome constante,unidade constante,quantidade variavel,preco por unidade para soma de gastos
    def __init__(self,nome=None,unidade=None,quantidade=0,gasto=0,preco_unitario=0):
        self.nome = nome
        self.unidade = unidade
        self.quantidade = quantidade
        self.gasto = gasto
        self.preco_unitario = preco_unitario
        self.precos_lista = []
        self.preco_media = 0
        self.precos = 0.0

    def retorna_nome(self):
        print(self.nome)
        return self.nome

    def entra_estoque(self,quantidade,preco):
        self.preco_unitario = preco/quantidade
        self.precos_lista.append(self.preco_unitario)
        if self in estoque:
            self.quantidade += quantidade
        else:
            estoque.append(self)
            self.entra_estoque(quantidade,preco)


    def calcula_preco_media(self):
        for preco in self.precos_lista:
            self.precos += preco
        self.preco_media = self.precos / len(self.precos_lista)
        print(f'{self.preco_media:.2f}')
        return self.preco_media


while True:
    print(f'[1]adicionar item\n[2]adicionar ao estoque\n[3]remover do estoque\n[4]mostrar estoque')
    escolha = int(input('escolha o menu: '))
    if escolha == 1:
        nome = str(input('digite o nome do produto: ')).strip
        unid = str(input(f'digite a forma de controle de estoque\npermitidos={unidades}: ')).strip
        prod = Produto(nome,unid)
        produtos.append(prod)
    elif escolha == 2:
        escolha_prod = str(input('digite o nome do produto: ')).strip
        escolha_quant = int(input('digite a quantidade: ')).strip
