# DESAFIO 060
num = int(input('Digite um numero: '))
f = 1
flag = num

while flag > 0:
    f *= flag
    flag -= 1

print('{}! = {}' .format(num, f))
