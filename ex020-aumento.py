#DESAFIO 034
sal = float(input('Qual o salário?: '))
if sal > 1250:
    novoSal = sal*1.10
    print('Novo salário: {:.2f}R$' .format(novoSal))
else:
    novoSal = sal*1.15
    print('Novo salário: {:.2f}R$' .format(novoSal))