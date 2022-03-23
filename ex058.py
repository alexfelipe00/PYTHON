# DESAFIO 084
pessoas = []
pesados = []
leves = []
temp = []
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    pessoas.append(temp[:])
    if temp[1] >= 100:
        pesados.append(temp[:])
    elif temp[1] <= 50:
        leves.append(temp[:])
    temp.clear()
    op = input('Add mais ?[s/n]: ').upper()
    if op == 'N':
        break

print('-'*60)
print(f'{len(pessoas)} foram cadastradas.')

if len(pesados) > 0:
    print(f"Pessoas acima de 100kg's: ")
    for c in pesados:
        print(f'{c[0]} tem {c[1]}kg')
if len(leves) > 0:
    print(f"Pessoas abaixo de 50kg's: ")
    for c in leves:
        print(f'{c[0]} tem {c[1]}kg')

print(pessoas)