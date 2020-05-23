cons = float(input("Consumo de energia: "))
tipo = input("(R) para resisd. / (I) para indus. / (C) para comerc. / Tipo: ")
print("Entradas: ", cons, "kWh e tipo ", tipo)

if (cons > 0):
	if (tipo == "R"):
		if (cons <= 500):
			var = round(0.44*cons, 2)
		if (cons > 500):
			var = round(0.65*cons, 2)
		print("Valor total: R$", var)
	elif (tipo == "C"):
		if (cons <= 1000):
			var = round(0.55*cons, 2)
		if (cons > 1000):
			var = round(0.60*cons, 2)
		print("Valor total: R$", var)
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")
