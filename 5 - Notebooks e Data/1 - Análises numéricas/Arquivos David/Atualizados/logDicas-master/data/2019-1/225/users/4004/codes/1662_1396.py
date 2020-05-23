consumo = float(input("valor consumido: "))

if consumo <= 300.0:
	gorjeta = consumo + (consumo/10)
	print(round(gorjeta, 2))
else:
	gorjeta = consumo + ((consumo/100)*6)
	print(round(gorjeta, 2))