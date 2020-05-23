consumo = float(input("consumo de energia: "))
tipo = input("tipo de instalacao: ").upper()

if consumo < 0:
	if tipo != "R" or tipo != "I" or tipo != "C":
		print("Entradas: ", consumo, "kWh e tipo", tipo)
		print("Dados invalidos")
	
elif consumo > 0:
	if tipo == "R":
		if consumo <= 500:
			c = consumo * 0.44
		else:
			c = consumo * 0.65
		c = round(c,2)
		print("Entradas: ", consumo,"kWh e tipo", tipo)
		print("Valor total: R$ ",c)

	if tipo == "I":
		if consumo <= 1000:
			c = consumo * 0.55
		else:
			c = consumo * 0.60
		c = round(c,2)
		print("Entradas: ", consumo,"kWh e tipo", tipo)
		print("Valor total: R$ ",c)

	if tipo == "C":
		if consumo <= 5000:
			c = consumo * 0.55
		else:
			c = consumo * 0.60
		c = round(c,2)
		print("Entradas: ", consumo,"kWh e tipo", tipo)
		print("Valor total: R$ ",c)