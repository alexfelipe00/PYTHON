#DESAFIO 059
flag = 0

v1 = float(input('Digite o 1º número: '))
v2 = float(input('Digite o 2º número: '))
while flag != 5:
    op = int(input('------- MENU -------\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5]Sair do programa\n: '))
    if op == 1:
        print('{} + {} = {}' .format(v1, v2, v1+v2))
    elif op == 2:
        print('{} x {} = {}' .format(v1, v2, v1*v2))
    elif op == 3:
        if v1 > v2:
            print('{} > {}' .format(v1, v2))
        else:
            print('{} > {}' .format(v2, v1))
    elif op == 4:
        v1 = float(input('Digite o 1º número: '))
        v2 = float(input('Digite o 2º número: '))
    elif op == 5:
        flag = 5
    else:
        print('Digite um valor válido.')