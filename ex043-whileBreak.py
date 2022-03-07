# DESAFIO 066
soma = 0
flag = 0
n = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break

    soma += n
    flag += 1
print(f'Foram digitados {flag} numeros\n{soma} somando todos.')
