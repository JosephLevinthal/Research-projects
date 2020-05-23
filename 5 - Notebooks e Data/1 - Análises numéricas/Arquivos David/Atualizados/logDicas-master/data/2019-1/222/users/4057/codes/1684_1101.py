# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
X = float(input("Qual o consumo de energia em kWh: "))
Y = input("O tipo de instalacao (R para residencias, I para industrias, e C para comercios): ")
if (Y.upper() == "R"):
	if (X > 1) and (X <= 500) :
		Z = X * 0.44
		print("Entradas: ", X, "kWh e tipo ", Y.upper())
		print("Valor total: R$ ", round(Z, 2))
	elif (X > 500):
		Z = X * 0.65
		print("Entradas: ", X, "kWh e tipo ", Y.upper())
		print("Valor total: R$ ",round(Z, 2))
	else: 
		print("Entradas: ", X, "kWh e tipo ", Y.upper())
		print("Dados invalidos")
elif (Y.upper() == "C"):
	if (X > 1) and(X <= 1000) :
		Z = X * 0.55
		print("Entradas: ", X, "kWh e tipo ", Y.upper())
		print("Valor total: R$ ",round(Z, 2))
	elif X > 1000 :
		Z = X * 0.60
		print("Entradas: ", X, "kWh e tipo ", Y.upper())
		print("Valor total: R$ ",round(Z, 2))
	else: 
		print("Entradas: ", X, "kWh e tipo ", Y.upper())
		print("Dados invalidos")
elif (Y.upper() == "I"):
	if (X> 1) and (X <= 5000) :
		Z = X * 0.55
		print("Entradas: ", X, "kWh e tipo ", Y.upper())
		print("Valor total: R$ ",round(Z, 2))
	elif X > 5000 :
		Z = X * 0.60
		print("Entradas: ", X, "kWh e tipo ", Y.upper())
		print("Valor total: R$ ",round(Z, 2))
	else: 
		print("Entradas: ", X, "kWh e tipo ", Y.upper())
		print("Dados invalidos")
else: 
	print("Entradas: ", X, "kWh e tipo ", Y.upper())
	print("Dados invalidos")