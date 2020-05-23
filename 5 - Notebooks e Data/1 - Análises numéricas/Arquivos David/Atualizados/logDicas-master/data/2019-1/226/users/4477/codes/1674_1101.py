consumo = float(input("digite o consumo: "))
tipo = input("tipo de instalacao: (R/I/C) ")

print("Entradas:", consumo, "kWh e tipo", tipo.upper())

if (consumo < 0):
	print("Dados invalidos")
elif (tipo.upper() == "R"):
	if (consumo <= 500):
			x = consumo*0.44
			y = round(x, 2)
			print("Valor total: R$", y)
	else:
		x = consumo*0.65
		y = round(x, 2)
		print("Valor total: R$", y)
elif (tipo.upper() == "C"):
	if (consumo <= 1000):
		x = consumo*0.55
		y = round(x, 2)
		print("Valor total: R$", y)
	else:
		x = consumo*0.60
		y = round(x, 2)
		print("Valor total: R$", y)
elif (tipo.upper() == "I"):
	if (consumo <= 5000):
		x = consumo*0.55
		y = round(x, 2)
		print("Valor total: R$", y)
	else:
		x = consumo*0.60
		y = round(x, 2)
		print("Valor total: R$", y)