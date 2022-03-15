# DESAFIO 078

num = []
maior = 0
menor = 0

for c in range(0, 5):
    num.append(int(input(f'Digite o valor {c}: ')))
    if c == 0:
        mai =  num[c]
        menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]

print('*=' * 30)
print(f'Você digitou a lista: {num}')
print(f'Maior valor da lista: {maior} nas posições', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f' {i},', end='')
print()
print(f'Menor valor da lista: {menor} nas posições', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f' {i},', end='')