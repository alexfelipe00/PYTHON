# DESAFIO 088
import os
import random
from time import sleep

cartela = []
temp = []
nJogadas = numero = tot = 0

print('-'*30)
print(f"{'Joga na MEGA SENA':^30}")
print('¨'*30)
nJogadas = int(input('Quantos jogos ?: '))
print('¨'*30)
print(f'*- Sorteando {nJogadas} jogos -*')

while tot < nJogadas:
    cont = 0
    while True:
        numero = random.randint(1, 60)
        if numero not in temp:
            temp.append(numero)
            cont += 1
        if cont == 6:
            break
    temp.sort()
    cartela.append(temp[:])
    temp.clear()
    tot += 1

for n in range(0, len(cartela)):
    print(f'Jogo {n+1}: ', end='')
    for i in cartela[n]:
        print(f'({i}) ', end='')
    print()
    sleep(0.6)
os.system("pause")