# DESAFIO 058
import random

flag = 1
r = 1
valorJ = 0
valorPC = random.randint(1, 10)

while flag == 1:
    valorJ = int(input('Digite um valor: '))
    if valorPC == valorJ:
        print(' ------- ACERTOU ! ------- ')
        flag = 0
    elif valorPC > valorJ:
        print('Mais... Tente mais uma vez. ')
        r += 1
    else:
        print('Menos... Tente mais uma vez')
        r += 1
print('Precisou jogar {} vezes para acertar' .format(r))
