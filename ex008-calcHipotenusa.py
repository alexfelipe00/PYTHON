import math

# DESAFIO 017
print('Calculadora de hipotenusa')
c1 = float(input('Digite o tamanho do cateto 1: '))
c2 = float(input('Digite o tamanho do cateto 2: '))
hi = math.hypot(c1, c2)

print('Valor da hipotenusa é: {}' .format(hi))
