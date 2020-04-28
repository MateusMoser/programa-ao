#programa para fazer calculo de tinta de um loja
import math



class Calculadora_tintas(object):
    def __init__(self,lata_grande,lata_pequena,valor_grande,valor_pequena):
        self.lata_grande = lata_grande
        self.lata_pequena = lata_pequena
        self.valor_grande = valor_grande
        self.valor_pequena = valor_pequena
        

    def calc_lata_grande(self,quantidade):
        #QUANTIDADE EM litros
        self.quantidade_grande = quantidade//self.lata_grande
        math.ceil(self.quantidade_grande)
        self.valor = self.quantidade_grande*self.valor_grande
        print(f'Voce precisa comprar {self.quantidade_grande} latas grandes  \tValor = {self.valor}')
        return self.valor

    def calc_lata_pequena(self,quantidade):
        #QUANTIDADE EM  litros
        self.quantidade_pequena = quantidade // self.lata_pequena
        math.ceil(self.quantidade_pequena)
        self.valor = self.quantidade_pequena*self.valor_grande
        print(f'Voce precisa comprar {self.valor_pequena} latas pequenas\t Valor = {self.valor}')
        return self.valor

    def calc_misto(self,quantidade):
        if quantidade > self.lata_pequena:
            self.quantidade_grande = int(quantidade / self.lata_grande)
            self.resto =  quantidade - (self.quantidade_grande*self.lata_grande) 
            if self.resto > 0:
                self.quantidade_pequena = math.ceil(self.resto / self.lata_pequena)
                print(f'Voce usara:\n{self.quantidade_grande} latas grandes\n{self.quantidade_pequena} latas pequenas\nO valor total ficara em {(self.valor_grande*self.quantidade_grande)+(self.quantidade_pequena*self.valor_pequena)} ')
            else:
                print(f'{self.quantidade_grande} Latas grandes \tvalor={self.valor_grande*self.quantidade_grande}')
        else:
            print(f'voce precisa apenas de 1 lata pequena \t valor={self.valor_pequena}')
            
            
Loja_Juca = Calculadora_tintas(16,4,70,20)
loja_breno = Calculadora_tintas(24,8,100,32)

Loja_Juca.calc_misto(60)
loja_breno.calc_misto(60)
