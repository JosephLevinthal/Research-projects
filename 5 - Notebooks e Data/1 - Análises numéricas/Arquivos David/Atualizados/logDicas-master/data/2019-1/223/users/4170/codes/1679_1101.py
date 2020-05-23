# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("Consumo de energia: "))
y = input("Tipo de instalacao: ")
print("Entradas:", x, "kWh e tipo", y)
if((y == "R" or y == "I" or y == "C") and (x > 0)):
	if ((x <= 500) and (y == "R")):
		total = x * 0.44
		print("Valor total: R$", round(total,2))
	elif((x > 500) and (y == "R")):
		total = x * 0.65
		print("Valor total: R$", round(total,2))
	elif((x <= 1000) and (y == "C")):
		total = x * 0.55
		print("Valor total: R$", round(total,2))
	elif((x > 1000) and (y == "C")):
		total = x * 0.60
		print("Valor total: R$", round(total,2))
	elif((x <= 5000) and (y == "I")):
		total = x * 0.55
		print("Valor total: R$", round(total,2))
	elif((x > 5000) and (y == "I")):
		total = x * 0.60
		print("Valor total: R$", round(total,2))
else:
	print("Dados invalidos")