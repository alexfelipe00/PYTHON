
#PEQUENA = 15R$          MÉDIA = 17R$      GRANDE = 19R$
#Sobra deve comprar camisas pequenas

'''Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo
vendidas respectivamente por 15, 17 e 19 reais. Um usuário deseja gastar Y reais de
maneira que compre mais camisetas pequenas, poucas grandes e outras médias. Informar
quantas camisetas poderão ser compradas e seus tipos.'''
#  70% pequenas, 25% médias, 5% pequenas

qtoP = qtoM = qtoG = sobra = 0

valor = int(input('Valor: '))

qtoP = int(((valor*70)/100)/15) 
qtoM = int(((valor*25)/100)/17) 
qtoG = int(((valor*5)/100)/19) 

sobra = (((valor*70)/100)%15) + (((valor*25)/100)%17) + (((valor*5)/100)%19)

if sobra > 15:
    qtoP += int(sobra/15)
    sobra = sobra%15

print(f'{qtoP} Camisas pequenas\n{qtoM} Camisetas médias\n{qtoG} Camisetas grandes\n\nSobrou {sobra:.2f}R$')