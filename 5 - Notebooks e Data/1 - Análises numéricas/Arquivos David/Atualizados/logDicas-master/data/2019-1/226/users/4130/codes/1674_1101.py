x = float(input("Digite o consumo em kWh: "))
y = input("Digite o tipo da instalacao (R, I, C): ").upper()

print("Entradas: ",x, "kWh e tipo",y)

if (y == "R") and (x > 0):
	if(x <= 500):
		z = x * 0.44
		print("Valor total: R$",round(z, 2))
	elif(x > 500):
		z = x * 0.65
		print("Valor total: R$",round(z, 2))
elif(y == "C") and (x > 0):
	if(x <= 1000):
		z = x * 0.55
		print("Valor total: R$",round(z, 2))
	elif(x > 1000):
		z = x * 0.6
		print("Valor total: R$",round(z, 2))
elif(y == "I") and (x > 0):
	if(x <= 5000):
		z = x * 0.55
		print("Valor total: R$",round(z, 2))
	elif(x > 5000):
		z = x * 0.6
		print("Valor total: R$",round(z, 2))
else:
	print("Dados invalidos")