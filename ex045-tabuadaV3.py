#DESAFIO 067

while True:
    v = int(input('Quer ver tabuada de qual valor ?: '))
    if v <= 0:
        print('-='*20)
        print('PROGRAMA TABUADA ENCERRADO.')
        break
    print('-='*20)
    for c in range(0, 10):
        print(f'{v} x {c} = {v*c}')
