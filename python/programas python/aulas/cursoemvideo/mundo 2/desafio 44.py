print ('{:=^40}'.format('lojas guanaraba'))
price = (int(input('qual o preço da compra? ')))
print ('formas de pagamento')
print ('[1] a vista no dinheiro ou cheque')
print ('[2] a vista no cartao')
print ('[3] 2x no cartao')
print ('[4] 3x ou mais no cartao')
esc = (int(input('qual a sua escolha?')))
if esc == 1:
    calc = price * 0.9
    print ('voce ira pagar apenas {}'.format(calc))
elif esc == 2:
    calc = price * 0.95
    print ('voce ira pagar apenas {}'.format(calc))
elif esc == 3:
    print ('voce ira pagar o preço normal que é {}'.format(price))
elif esc == 4:
    calc = price * 1.20
    print ('voce ira pagar {}'.format(calc))