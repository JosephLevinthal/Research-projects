ce = float(input(""))
y = input("")
print("Entradas:", ce, "kWh e tipo", y)

if ((ce < 0) or (y != "R") and (y != "I") and (y != "C")):
	print("Dados invalidos")
elif ((y == "R") and (ce <= 500)):
	conta = ce * 0.44
	print("Valor total: R$", round(conta, 2))
elif ((y == "R") and (ce > 500)):
	conta = ce * 0.65
	print("Valor total: R$", round(conta, 2))
elif ((y == "I") and (ce <= 5000)):
	conta = ce * 0.55
	print("Valor total: R$", round(conta, 2))
elif ((y == "I") and (ce > 5000)):
	conta = ce * 0.60
	print("Valor total: R$", round(conta, 2))
elif ((y == "C") and (ce <= 1000)):
	conta = ce * 0.55
	print("Valor total: R$", round(conta, 2))
elif ((y == "C") and (ce > 1000)):
	conta = ce * 0.60
	print("Valor total: R$", round(conta, 2))