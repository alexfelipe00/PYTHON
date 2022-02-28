#DESAFIO 036
valorCasa = float(input('Valor da casa: '))
sal = float(input('Salário: '))
tempo = int(input('Parcelar em quantos anos: '))
valorMen = valorCasa/sal
porSal = sal*0.3
print('=-'*20)
if valorMen > porSal:
    print('Valor casa: {}R$\nSalário: {}R$\nValor Mensal: {:.3f}R$\nValor da parcela excede 30% do seu salario. Pedido negado.' .format(valorCasa, sal, valorMen))
else:
    print('Valor casa: {}R$\nSalário: {}R$\nValor Mensal: {:.3f}R$\nEmprestimo aprovado.' .format(valorCasa, sal, valorMen))
print('=-'*20)