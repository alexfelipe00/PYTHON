#DESAFIO 071
print('='*10, 'Banco Alex', '='*10)
valor = int(input('Que valor quer sacar ?R$ '))
n200 = n100 = n50 = n20 = n10 = n5 = n1 = 0

n200 = valor//200
n100 = (valor%200)//100
n50 = ((valor%200)%100)//50
n20 = (((valor%200)%100)%50)//20
n10 = ((((valor%200)%100)%50)%20)//10
n5 = (((((valor%200)%100)%50)%20)%10)//5
n1 = ((((((valor%200)%100)%50)%20)%10)%5)//1
if n200 !=0:
    print(f'Notas de 200R$: {n200}')
if n100 !=0:
    print(f'Notas de 100R$: {n100}')
if n50 !=0:
    print(f'Notas de 50R$: {n50}')
if n20 !=0:
    print(f'Notas de 20R$: {n20}')
if n10 !=0:
    print(f'Notas de 10R$: {n10}')
if n5 !=0:
    print(f'Notas de 5R$: {n5}')
if n1 !=0:
    print(f'Notas de 1R$: {n1}')
