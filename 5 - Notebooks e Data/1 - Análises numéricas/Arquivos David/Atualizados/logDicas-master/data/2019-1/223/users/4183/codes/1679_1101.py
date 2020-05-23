X = float(input("Qual o consumo? "))
Y = input("TIPO: R-Residencial , C-Comercial , I-Industrial ")
preco = 0
if (X <= 0)or (not (Y  == "R") and not (Y == "C") and not (Y == "I")):
	print("Entradas:", X, "kWh e tipo", Y)
	print("Dados invalidos")
elif (Y == "R"):
	if (X <= 500): 
		preco = 0.44
	else:
		preco = 0.65
elif (Y == "C"):
	if (X <= 1000): 
		preco = 0.55
	else:
	 	preco = 0.60
elif (X <= 5000):
	if (X <= 500): 
		preco = 0.55
	else:
		preco = 0.60
if (preco > 0):
	print("Entradas:", X, "kWh e tipo", Y)
	print("Valor total: R$", round(preco*X,2))
