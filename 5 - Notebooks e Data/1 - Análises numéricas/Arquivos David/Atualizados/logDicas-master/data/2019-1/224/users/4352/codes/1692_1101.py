consumo = float(input("digite o consumo de energia em kwh: "))
tipo = input("digite o tipo de instalacao: (R/C/I)")
print("Entradas:",consumo,"kWh e tipo",tipo.upper())
if consumo <= 500 and consumo>0 and tipo.upper() == "R":
	a = consumo * .44
	print("Valor total: R$", round(a, 2))
elif consumo > 500 and consumo>0 and tipo.upper() == "R":
	b = consumo * .65
	print("Valor total: R$", round(b, 2))
elif consumo <= 1000 and consumo>0 and tipo.upper() == "C":
	c = consumo * .55
	print("Valor total: R$", round(c, 2))
elif consumo > 1000 and consumo>0 and tipo.upper() == "C":
	d = consumo * .60
	print("Valor total: R$", round(d, 2))
elif consumo <= 5000 and consumo>0 and tipo.upper() == "I":
	e = consumo * .55
	print("Valor total: R$", round(e, 2))
elif consumo > 5000 and consumo>0 and tipo.upper() == "I":
	f = consumo * .60
	print("Valor total: R$", round(f, 2))
else:
	print("Dados invalidos")
