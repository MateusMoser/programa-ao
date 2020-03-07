from random import randint


def sorteio(lista):
    for _ in range(5):
        lista.append(randint(1, 10))
    print(lista)


def somapar(nums):
    pares = [n for n in nums if n % 2 == 0]
    print(f'Os numeros pares sao {pares}')


numeros = []
sorteio(numeros)
somapar(numeros)
