#DESAFIO 044
print('-='*40)
val = float(input('Digite o valor da compra: '))
print('Escolha o modo de pagamento:\n1 - Á vista dinheiro/cheque: 10% de desconto\n2 - Á vista no cartão: 5% de desconto\n3 - 2x no cartão: Preço normal\n4 - 3x ou mais no cartão: 20% de juros.')
op = int(input('Escolha uma opção de pagamento: '))

avista = val*0.9
avistaC = val*0.95
tresXC = val*1.2
print('-='*40)
if op == 1:
    print('Valor da compra: {}R$      Valor final ({}R$ de desconto): {}R$' .format(val, val-avista ,avista))
elif op == 2:
    print('Valor da compra: {}R$      Valor final ({}R$ de desconto): {}R$' .format(val, val-avistaC ,avistaC))
elif op == 3:
    print('Valor final: {}R$' .format(val))
elif op == 4:
    print('Valor da compra: {}R$      Valor final ({}R$ de juros): {}R$' .format(val, tresXC-val ,tresXC))
else:
    print('Digitou uma opção inválida')
print('-='*40)