galera = [['Jão', 19], ['Ana', 34], ['Andre', 18], ['Maria', 28], ['Junior', 57]]
print(galera) #todos os elementos
print(galera[0]) #todos os dados do elemento 0
print(galera[0][0]) #primeiro elemento e primeiro subelemento
print('')

dadosTemp = []
for c in range(0, 2):
    dadosTemp.append(input('Nome: '))
    dadosTemp.append(input('Idade: '))
    galera.append(dadosTemp[:])
    dadosTemp.clear()

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade') 
