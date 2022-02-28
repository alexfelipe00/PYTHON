import math

#DESAFIO 018
ang = float(input('Digite um ângulo qualquer: '))


sen = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('    {}°\nSeno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}' .format(ang, sen, coss, tang))
