#DESAFIO 024
num = str((int(input('Digite um numero entre 0-9999: ')))/1000)
print('Unidade: {}' .format(num[4]))
print('Dezena: {}' .format(num[3]))
print('Centena: {}' .format(num[2]))
print('Milhar: {}' .format(num[0]))