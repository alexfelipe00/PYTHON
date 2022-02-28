#DESAFIO 039
from datetime import datetime
anoNasc = input('Digite seu ano de nascimento (dd/mm/aaaa) : ')
anoNasc = datetime.strptime(anoNasc, '%d/%m/%Y') #converte string para datetime
dataAtual = (datetime.now().strftime('%d/%m/%Y'))
dataAtual = datetime.strptime(dataAtual, '%d/%m/%Y') #converte string para datetime
qtoDias = int(abs(((anoNasc - dataAtual).days)/365))
if qtoDias < 18:
    print('Não precisa se alistar, faltam {:.0f} ano(s) para realizar o alistamento' .format(18-qtoDias))
elif qtoDias == 18:
    print('Você deve se alistar esse ano, procure a data e o local de sua cidade')
else:
    print('Fazem {:.0f} ano(s) do seu prazo de alistamento' .format(qtoDias-18))