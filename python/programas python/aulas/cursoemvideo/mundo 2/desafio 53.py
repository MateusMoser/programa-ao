frase = str(input('digite uma frase')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('a frase é um palindromo')
else:
    print('a frase nao é um palimdromo')