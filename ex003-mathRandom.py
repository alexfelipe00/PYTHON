import math
import random
import emoji

# DESAFIO 006
# randint: gera numeros randomicos no intervalo definido
num = random.randint(1, 10)
dobro = num*2
triplo = num*3
potencia = math.pow(num, 2)
raiz = math.sqrt(num)
print('{} x 2 = {}' .format(num, dobro))
print('{} x 3 = {}' .format(num, triplo))
print('{}² = {}' .format(num, potencia))
print('√{} = {}' .format(num, raiz))

print(emoji.emojize("Olá mundo :earth_americas:", use_aliases=True))
