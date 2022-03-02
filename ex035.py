# DESAFIO 054
from datetime import date

atual = date.today().year
totMaior = 0
totMenor = 0
for pos in range(0, 4):
    nasc = int(input('Em que ano a {}ª pessoa nasceu ?: ' .format(pos + 1)))
    idade = atual - nasc
    if idade < 18:
        totMenor += 1
    else:
        totMaior += 1
print('{} são MAIORES de idade\n{} são MENORES de idade' .format(totMaior, totMenor))
