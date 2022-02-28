#DESAFIO 037
num = int(input('Digite um numero: '))
print('1 para binário\n 2 para octal\n3 para hexadecimal\n4 todas as opções')
op = int(input('Escolha a base desejada: '))
b = bin(num)
o = oct(num)
h = hex(num)
if op == 1:
    print(b[2:])
elif op == 2:
    print(o[2:])
elif op == 3:
    print(h[2:])
elif op == 4:
    print('Binário: {}' .format(b[2:]))
    print('Octal: {}' .format(o[2:]))
    print('Hexadecímal: {}' .format(h[2:]))
else:
    print('Digitou uma opção inválida')