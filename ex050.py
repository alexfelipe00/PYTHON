# DESAFIO 075

num = (int(input('1º numero: ')), int(input('2º numero: ')),
       int(input('3º numero: ')), int(input('4º numero: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O valor 3 apareceu {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado.')

print('Os valores pares digitados foram: ', end='')
for n in num:
    if n%2 == 0:
        print(f'{n} ', end='')