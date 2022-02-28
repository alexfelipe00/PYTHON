# DESAFIO 012
vp = int(input('Preço do produto: '))
vd = int(input('Desconto (%): '))

valorDesconto = vp * (vd/100)
valorFinal = vp - valorDesconto
print('Valor inicial {}R$\nValor com desconto de {}% = {}R$' .format(vp, vd, valorFinal))
