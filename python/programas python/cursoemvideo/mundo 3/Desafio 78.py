nums = list()
maior = 0
menor = 0
for c in range(0,5):
    nums.append(input('Digite um valor'))
print(f'Os valores digitados foram {nums}')
print(f'O maior valore foi {max(nums)} nas posiçoes {nums.index(max(nums))+1}')
print(f'O menor valor foi {min(nums)} na posiçao {nums.index((min(nums)))+1}')
