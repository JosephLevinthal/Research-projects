x = float(input("consumo de energia: "))
y = input("tipo de instalacao: ").upper()
print("Entradas:", x, "kWh e tipo", y)
if((x >= 0) and ((y == "R") or (y == "C") or (y == "I"))):
	if((x <= 500) and (y == "R")):
		z = round(x * 0.44, 2)
		print("Valor total: R$", z)
	elif((x > 500) and (y == "R")):
		z = round(x * 0.65, 2)
		print("Valor total: R$", z)
	elif((x <= 1000) and (y == "C")):
		z = round(x * 0.55, 2)
		print("Valor total: R$", z)
	elif((x > 1000) and (y == "C")):
		z = round(x * 0.60, 2)
		print("Valor total: R$", z)
	elif((x <= 5000) and (y == "I")):
		z = round(x * 0.55, 2)
		print("Valor total: R$", z)
	elif((x > 5000) and (y == "I")):
		z = round(x * 0.60, 2)
		print("Valor total: R$", z)
else:
	print("Dados invalidos")