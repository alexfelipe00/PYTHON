#DESAFIO 029
vel = int(input('Digite a valocidade do automovél KM/h: '))
if vel > 80:
    multa = (vel - 80)*7
    print('Excedeu a velocidade permitida X\nMultado no valor de {}R$' .format(multa))
else:
    print('Velocidade permitida na via')