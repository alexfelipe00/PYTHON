# DESAFIO 076

lista = ('Pão', 3.5,
         'Pizza Seara', 13.60,
         'Chinelo Havaianas', 30,
         'Maionese Hellmanns', 8, 
         'Pringles Churrasco', 18)
total = 0
cifrão = 'R$'
print('='*60)
print(f"{'Recibo MercadoFodase':^60}\a")
print('='*60)


for c in range(0, len(lista)):
    if c % 2 == 0:
        print('{:_<53}' .format(lista[c]), end='')
        
    else:
        total += lista[c]
        print('R${:>5.2f}' .format(lista[c]))

print('\n', '-'*59)
print(f'"TOTAL {cifrão:>45}{total:.2f}')
print('-'*59)
