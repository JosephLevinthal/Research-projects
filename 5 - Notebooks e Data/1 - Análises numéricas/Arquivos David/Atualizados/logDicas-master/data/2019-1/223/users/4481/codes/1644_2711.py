a = int(input('valores: '))
b = int(input('quantidade tickets: '))
c = float(input('valor tickets: '))
d = int(input('quant de onibus: '))
e = float(input('valor passes: '))
soma = ( a - (b * c + d * e))
if(soma >= 0):
	print('SUFICIENTE')
else:
	print('INSUFICIENTE')