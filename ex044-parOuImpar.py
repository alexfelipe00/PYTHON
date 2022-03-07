#DESAFIO 68
import random

num = 1
flag = 0

while num > 0:
    numPC = random.randint(0, 5)
    num = int(input('Diga um valor: '))
    op = input('Par ou Ímpar ? [P/I]: ').upper()
    resultado = (num + numPC) % 2
    print(f'Você jogou {num} e o computador {numPC}.')
    if resultado == 0:
        print(f'{num+numPC} é PAR', end=' - ')
    else:
        print(f'{num+numPC} é ÍMPAR', end=' - ')
    if op == 'P' and resultado == 0 or op == 'I' and resultado == 1:
        print('Você VENCEU !\nVamos jogar novamente...')
        print('-='*20)
        flag += 1
    else:
        print('Você PERDEU !')
        print('-='*20)
        break

print(f'GAME OVER ! Você venceu {flag} vez(es).')
