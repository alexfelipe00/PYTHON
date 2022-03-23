#DESAFIO 086
matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
somaPares = somaTerceira = maiorValor = segundaLinha = 0 

for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a [{l+1}][{c+1}]: '))

print('-'*60)

for l in range(0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-'*60)

for l in range(0,3):
    for c in range (0,3):
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
        if c == 2:
            somaTerceira += matriz[l][c]
        if l == 1 and matriz[l][c] > maiorValor:
            maiorValor = matriz[l][c]

print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaTerceira}')
print(f'O maior valor da segunda linha é {maiorValor}')
