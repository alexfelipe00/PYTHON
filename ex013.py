#DESAFIO 022
nome = input('Digite um nome: ')
print(nome.upper())
print(nome.lower())
print('Quant. de letras: {}' .format(len(nome.replace(' ', ''))))
nomDividido = nome.split()
print('Quant. letras no primeiro nome: {}' .format(len(nomDividido[0])))