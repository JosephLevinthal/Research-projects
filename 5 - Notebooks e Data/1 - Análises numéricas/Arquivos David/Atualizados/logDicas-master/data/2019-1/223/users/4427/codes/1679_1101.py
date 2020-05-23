# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

consumo = float(input("consumo de energia (em kWh): "))
tipo = input("tipo de instalacao (R para residencias, I para industrias, e C para comercios): ")
calculo = float()

if consumo >= 0:
	if tipo == "R":
		if consumo <= 500:
			calculo = (consumo*0.44)
			print("Entradas: ", consumo, "kWh e", "tipo", tipo)
			print("Valor total: R$ %.2f" %calculo)
		else:
			calculo = consumo*0.65
			print("Entradas: ", consumo, "kWh e", "tipo ", tipo)
			print("Valor total: R$ %.2f" %calculo)
	elif tipo == "I":
		if consumo <=1000:
			calculo = consumo*(0.55)
			print("Entradas: ", consumo, "kWh e", "tipo ", tipo)
			print("Valor total: R$ %.2f" %calculo)
		else:
			calculo = consumo*(0.60)
			print("Entradas: ", consumo, "kWh e", "tipo ", tipo)
			print("Valor total: R$ %.2f" %calculo)
	elif tipo == "C":
		if consumo <=5000:
			calculo = consumo*(0.55)
			print("Entradas: ", consumo, "kWh e", "tipo", tipo)
			print("Valor total: R$ %.2f" %calculo)
		else:
			calculo = consumo*(0.60)
			print("Entradas: ", consumo, "kWh e", "tipo", tipo)
			print("Valor total: R$ %.2f" %calculo)
	else:
		print("Entradas: ", consumo, "kWh e", "tipo", tipo)
		print("Dados invalidos")
else:
	print("Entradas: ", consumo, "kWh e", "tipo", tipo)
	print("Dados invalidos")

