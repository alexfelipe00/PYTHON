#DESAFIO 083
aberto = 0
fechado = 0
expressao = input('Digite uma expressão: ')
aberto = expressao.count('(')
fechado = expressao.count(')')

if aberto - fechado != 0:
    print(f'A expressão {expressao} é inválida')
else:
    print(f'{expressao} expressão correta.')