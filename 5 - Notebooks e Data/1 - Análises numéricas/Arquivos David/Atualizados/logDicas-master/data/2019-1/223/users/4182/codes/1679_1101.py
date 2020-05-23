consumo = float(input(""))
t = input("").upper()
print("Entradas: ", consumo, "kWh", "e", "tipo", t)

if (consumo > 0):
	if ((consumo <= 500) and (t == "R")):
		a = 0.44
		b = (consumo*a)
		print("Valor total: R$ ",round(b,2))
	elif ((consumo > 500) and (t == "R")):
		a = 0.65
		b = (consumo*a)
		print("Valor total: R$ ",round(b,2))
	elif ((consumo <= 1000) and (t == "C")):
		a = 0.55
		b = (consumo*a)
		print("Valor total: R$ ",round(b,2))
	elif ((consumo > 1000) and (t == "C")):
		a = 0.60
		b = (consumo*a)
		print("Valor total: R$ ",round(b,2))
	elif ((consumo <= 5000) and (t == "I")):
		a = 0.55
		b = (consumo*a)
		print("Valor total: R$ ",round(b,2))
	elif ((consumo > 5000) and (t == "I")):
		a = 0.60
		b = (consumo*a)
		print("Valor total: R$ ",round(b,2))
else:
	print("Dados invalidos")