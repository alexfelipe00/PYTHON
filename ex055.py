#DESAFIO 81
numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))
    op = input('Deseja digitar outro número ?[S/N]: ').upper()
    if op == 'N':
        break

if 5 in numeros:
    print('O 5 está entre os números')

print(f'Foram digitados {len(numeros)} números')

numeros.sort(reverse=True)
print(f'Valores em tamanho decrescente: {numeros}')