#DESAFIO 063

numTermos = int(input('Mostrar quantos termos da sequencia de fibonacci ? '))
flag = 0
f1 = 0
f2 = 1
fn = 0
while flag != numTermos:
    fn = f1 + f2
    if flag == 0:
        print('{}, {}, ' .format(f1, f2), end='')
    elif flag == numTermos-1:
        print('')
    else:
        print(', ')
    print('{}' .format(fn), end='')
    f1 = f2
    f2 = fn
    flag += 1
    