c = float(input("escreva o valor do consumo de energia: "))
if((c <= 150)):
	valor = (c * 0.60) + 5
	print (round(valor, 2))
elif((c >150) and (c <=250)):
	valor = (c * 0.65) + 8
	print (round(valor, 2)
elif((c >250) and (c <=350)):
	valor = (c * 0.70) + 12
	print (round(valor, 2))
else:
	valor = (c * 0.75) + 16
	print (round(valor, 2))

	