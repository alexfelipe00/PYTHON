#DESAFIO 058
import random

flag = 1
r = 1

valorJ = 0
while flag == 1:
    valorPC = random.randint(1,10)
    valorJ = int(input('Digite um valor: '))
    if valorPC == valorJ:
        print('Você {} - PC {}\n ------- ACERTOU ! ------- ' .format(valorJ, valorPC))
        flag = 0
    else:
        print('Você {} - PC {}\n ------- Errou ------- ' .format(valorJ, valorPC))
        print('Tente novamente.')
        r += 1
print('Precisou jogar {} vezes para acertar' .format(r))