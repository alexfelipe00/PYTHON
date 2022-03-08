#DESAFIO 072
numExt = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

dig = 1

while dig >= 0 and dig < 21:
    dig = int(input('Digite um numero entre 0 e 20: '))
    if dig >= 0 and dig < 21:
        print(f'{dig} por extenso é: {numExt[dig]}')
    else:
        print('Valor invalido. ', end='')
        dig = 1