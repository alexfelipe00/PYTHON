#DESAFIO 053
f = input('Digite uma frase: ').lower().strip()
dividido = f.split()
junto = ''.join(dividido)
inverso = ''
for letra in range(len(junto) - 1, - 1, -1):
    inverso += junto[letra]
if(inverso == junto):
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')

print(junto, inverso)
