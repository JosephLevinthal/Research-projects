consumo = float(input("consumo: "))
tipo = input("tipo:(R/I/C) ")
print("Entradas:", consumo, "kwh e tipo",tipo.upper())
if (consumo < 0):
	print("Dados invalidos")
elif (consumo <= 500) and (tipo == "R"):
	v = consumo * 0.44
	print("Valor total: R$", round(v, 2))
elif (consumo > 500) and (tipo == "R"):
	v = consumo * 0.65
	print("Valor total: R$", round(v, 2))
elif (consumo <= 1000) and (tipo == "C"):
	v = consumo * 0.55
	print("Valor total: R$", round(v, 2))
elif (consumo > 1000) and (tipo == "C"):
	v = consumo * 0.60
	print("Valor total: R$", round(v, 2))
elif (consumo <= 5000) and (tipo == "I"):
	v = consumo * 0.55
	print("Valor total: R$", round(v, 2))
elif (consumo > 5000) and (tipo == "I"):
	v = consumo * 0.60
	print("Valor total: R$", round(v, 2))
else:
	print("Dados invalidos")