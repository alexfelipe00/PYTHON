n1 = float(input('Digite a sua N1: '))
n2 = float(input('Digite sua n2: '))
m = (n1+n2)/2
print('Sua média é {:.1f}' .format(m))
if m >= 6 and m < 9:
    print('Muito bom')
elif m >= 9:
    print('PARABÉNS !!')
else:
    print('Vai estudar vagabundo >:( ')