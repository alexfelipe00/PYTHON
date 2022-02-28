#DESAFIO 035
a = float(input('Digite tamanho do lado A: '))
b = float(input('Digite tamanho do lado B: '))
c = float(input('Digite tamanho do lado C: '))

if abs(b-c) < a < (b+c) and abs(a-c) < b < (a+c) and abs(a-b) < c < (a+b):
    print('O triângulo EXISTE')
else:
    print('O triângulo NÃO EXISTE')