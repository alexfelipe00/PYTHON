#DESAFIO 055
maiorP = 0
menorP = 0 
for c in range(0, 5):
    p = float(input('Digite o peso da {}ª pessoa: ' .format(c)))
    if p >= maiorP:
        maiorP = p
    elif p < menorP:
        menorP = p
print('{:.1f}kg maior peso registrado\n{:.1f}kg menor peso registrado' .format(maiorP, menorP))