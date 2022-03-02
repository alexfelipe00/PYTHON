# DESAFIO 056

somaIdade = 0
maisVelho = 0
nomeVelho = ''
idadeMulher = 0
mediaIdade = 0
for p in range(0, 4):
    print('-=-=-= {}ª Pessoa =-=-=-' .format(p+1))
    nome = input('Digite o nome: ').upper().strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F): ')).upper().strip()
    somaIdade += idade
    if sexo == 'M' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome
    if sexo == 'F' and idade < 20:
        idadeMulher = + 1
mediaIdade = somaIdade/4
print('A média de idade do grupo é de {}' .format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}' .format(maisVelho, nomeVelho.title()))
print('Ao todo são {} mulheres com menos de 20 anos' .format(idadeMulher))
