# DESAFIO 042
a = float(input('Digite tamanho do lado A: '))
b = float(input('Digite tamanho do lado B: '))
c = float(input('Digite tamanho do lado C: '))

if abs(b-c) < a < (b+c) and abs(a-c) < b < (a+c) and abs(a-b) < c < (a+b):
    if a == b == c:
        print('Triângulo equilátero (Todos os lados iguais)')
    elif a == b != c or c == a != b or b == c != a:
        print('Triangulo isósceles (dois lados iguais)')
    else:
        print('Triangulo escaleno (todos os lados diferentes)')
else:
    print('O triângulo NÃO EXISTE')
