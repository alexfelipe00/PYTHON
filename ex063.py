# DESAFIO 089
ficha = []

while True:
    nome = input('Digite o nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    op = input('Add + [s/n]: ').upper()
    if op == 'N':
        break
    else:
        op = 'S'
print('¨'*22)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*22)
for i, n in enumerate(ficha):
    print(f'{i:<4}{n[0]:<10}{n[2]:>8.1f}')
