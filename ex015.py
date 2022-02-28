# DESAFIO 026
frase = (input('Digite uma frase: ')).lower().strip()
print('Nº de letra A: {}' .format(frase.count('a')))
print('Letra(a) aparece pela primeira vez na posição: {}' .format(frase.find('a')+1))
print('Letra(a) aparece pela última vez na posição: {}' .format(frase.rfind('a')+1))
