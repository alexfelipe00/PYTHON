#DESAFIO 79

num = []
fim = 1
op = 'S'

while op == 'S':
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print(f'Valor {n} adicionado.')
    else:
        print('Valor duplicado, digite outro numero.')
    
    op = input('Deseja adicionar outro número[S/N]: ').upper()
    if op == 'S':
        op = 'S'
    else:
        op == 'N'
        break

print('*-'*30)
num.sort()
print(f'VALORES: {num}')