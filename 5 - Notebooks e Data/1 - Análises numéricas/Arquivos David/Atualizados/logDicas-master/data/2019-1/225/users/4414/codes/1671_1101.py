x = float(input("Consumo de energia:"))
y = input("tipo de instalacao: R/I/C?").upper()
print("Entradas:",x,"kWh e tipo",y)
if(x<0) or not (y =="R" or y == "C" or y=="I"):
	print("Dados invalidos")
elif y == "R":
	if x < 500:
		z = x * 0.44
	else:
		z = x * 0.65
	z = round(z, 2)
	print("Valor total: R$", z)
elif y == "C":
	if x < 1000:
		z = x * 0.55
	else:
		z = x * 0.60
	z = round(z, 2)
	print("valor total: R$", z)
elif y == "I":	
	if x < 5000:
		z =  x * 0.55
	else:
		z = x * 0.60
	z = round(z, 2)
	print("Valor total:R$", z)