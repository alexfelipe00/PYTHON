xSalada = ('Salada', 'Tomate', 'Queijo', 'Hamburguer', 'Maionese')
molhos = ('BBQ', 'Cheedar')
for ingred in xSalada:
    print(f'{ingred}')

print('-'*30)

for c in range(0, len(xSalada)):
    print(f'{xSalada[c]}')

print(xSalada + molhos)