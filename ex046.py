# DESAFIO 070

op = 'S'
nomeMaisBarato = ''
totalValor = maisBarato = maisDeMil = 0

while op == 'S':
    produto = input('Nome do produto: ')
    valor = float(input('Preço: '))
    totalValor += valor
    if valor >= 1000:
        maisDeMil += 1
        nomeMaisBarato = produto
    op = input('Cadastrar mais ?(S/N): ').upper().strip()[0]
print('-='*10, 'FIM DO PROGRAMA', '-='*10)
print(f'Total da compra foi de R${totalValor:.2f}')
print(f'Temos {maisDeMil} custando mais de R$1000.00')
