# TIPOS PRIMITIVOS
#   int, float, bool, str
# OPERADORES ARITMETICOS
#    +   -   *   /   **   //   %

print('\n===== DESAFIO 01 =====')
num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
s = num1 + num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
e = num1 ** num2
r = num1 % num2
print('{} + {} = {}'.format(num1, num2, s))
print('{} * {} = {}' .format(num1, num2, m))
print('{} / {} = {:.3f}' .format(num1, num2, d))
print('{} // {} = {}' .format(num1, num2, di))
print('{} ^ {} = {}' .format(num1, num2, e))
print('{} % {} resto = {}' .format(num1, num2, r))
