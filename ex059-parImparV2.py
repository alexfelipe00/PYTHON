#DESAFIO 085
from queue import Empty


numeros = [[], []]
for c in range (0,4):
    temp = int(input('Digite um número: '))
    if temp % 2 == 0:
        numeros[0].append(temp)
    else:
        numeros[1].append(temp)


print('Números pares:')
if len(numeros[0]) == 0 :
    print('Nenhum.')
else:
    numeros[0].sort()
    print(numeros[0])
        
print('Números ímpares: ')
if len(numeros[1]) == 0 :
    print('Nenhum.')
else:
    numeros[1].sort()
    print(numeros[1])