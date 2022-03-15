num = [0, 8, 3, 7, 4, 1]
num2 = num[:] # NUM2 FAZ UMA CÓPIA DA LISTA NUM
num[1] = 9
num.append(10) # adiciona na ultima posição o valor 10
num.sort(reverse=True) # organiza a lista decrescente
num.insert(0, 1) # adiciona um elemento de valor 1 na posição 0
num.pop(5) # remove o elemento da posição 0

if 4 in num: # caso exista o 4 na lista
    num.remove(4) # remove a primeira ocorrencia do valor dentro do parâmetro
else:
    print('Não existe o número 4 na lista')
print(num)
print(f'Essa lista tem {len(num)} elementos')



valores = []
valores.append(1)
valores.append(5)
valores.append(3)

for v in valores:
    if v == (len(valores)):
        print(f'{v}', end='')
    else:
        print(f'{v} - ',  end='')
print('\n')
for c, v in enumerate(valores): # com enumerate retorna a posição do vetor e o conteúdo
    print(f'Na posição {c}, encontrei o valor {v}')



valoresDigitados = []
for cont in range(0, 5): # PREENCHER LISTA COM VALORES DIGITADOS
    valoresDigitados.append(int(input('Digite um valor: ')))

for c, v in enumerate(valoresDigitados):
    print(f'Na posição {c}, digitou o valor {v}')