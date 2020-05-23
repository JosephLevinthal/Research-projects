E = float(input("Consumo: "))
t = input("Tipo: ").upper()

print("Entradas:", E, "kWh e tipo", t)
y = "Dados invalidos"

if (((t != "R") and (t != "I") and (t != "C")) or (E < 0)):
	print(y)
elif ((t == "C") and (E <= 1000)):
	c = E*0.55
	print("Valor total: R$", round(c, 2))
elif ((t == "C") and (E > 1000)):
	c = E*0.60
	print("Valor total: R$", round(c, 2))
elif ((t == "R") and (E <= 500)):
	c = E*0.44
	print("Valor total: R$", round(c, 2))
elif ((t == "R") and (E > 500)):
	c = E*0.65
	print("Valor total: R$", round(c, 2))
elif ((t == "I") and (E <= 5000)):
	c = E*0.55
	print("Valor total: R$", round(c, 2))
elif ((t == "I") and (E > 5000)):
	c = E*0.60
	print("Valor total: R$", round(c, 2))
