import random

#DESAFIO 019
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('------------\nAluno escolhido foi: {}' .format(escolhido))

#DESAFIO 020
random.shuffle(lista)
print('A ordem de apresentação será: {}' .format(lista))