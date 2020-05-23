meses = 0
quantidade = int(input('quantidade inicial de pirarucus: '))
percent = int(input('percentual de crescimento no tanque: '))
while (0 < quantidade < 8000 ):
	acrescimo = quantidade * percent/100
	quantidade = quantidade + acrescimo
	quan = int(input('quantidade_retirada:'))
	quantidade = quantidade - quan
	meses += 1
if(quantidade <= 0):
	print ('ZERO')
else:
	print('MAXIMO')
print(meses)