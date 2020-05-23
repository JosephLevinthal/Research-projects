consumo = float(input("Consumo de energia: "))
tipo = input("O tipo de instalacao: ")
tipo= tipo.upper()
if(tipo == "R" and 0 <= consumo <=500):
	preco = consumo * 0.44
	print("Entradas:",consumo,"kWh  e tipo",tipo)
	print("valor total:  R$",round(preco, 2))
elif(tipo == "R" and consumo > 500):
	preco = consumo * 0.65
	print("Entradas:",consumo,"kWh  e tipo",tipo)
	print("valor total:  R$",round(preco, 2))
elif(tipo == "C" and 0 <= consumo <= 1000):
	preco = consumo * 0.55
	print("Entradas:",consumo,"kWh  e tipo",tipo)
	print("valor total:  R$", round(preco, 2))
elif(tipo == "C" and consumo > 1000):
	preco = consumo * 0.60
	print("Entradas:",consumo,"kWh  e tipo",tipo)
	print("valor total:  R$",round(preco, 2))
elif(tipo == "I" and 0 <= consumo <= 5000):
	preco = consumo * 0.55
	print("Entradas:",consumo,"kWh  e tipo",tipo)
	print("valor total:  R$",round(preco, 2))
elif(tipo == "I" and consumo > 5000):
	preco = consumo * 0.60
	print("Entradas:",consumo,"kWh  e tipo",tipo)
	print("valor total:  R$",round(preco, 2))
else:
	print("Entradas:",consumo,"kWh  e tipo",tipo)
	print("Dados invalidos ")