# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
consumo = float(input("Consumo de energia: "))
tipo = input("Tipo de instalacao: ")
tipo = tipo.upper()
if(tipo == "R" and 0 <= consumo <= 500):
	preco = consumo * 0.44
	print("Entradas:",consumo,"kWh e tipo",tipo)
	print("Valor total: R$",round(preco,2))
elif(tipo == "R" and consumo > 500):
	preco = consumo * 0.65
	print("Entradas:",consumo,"kWh e tipo",tipo)
	print("Valor total: R$",round(preco,2))
elif(tipo == "C" and 0 <= consumo <= 1000):
	preco = consumo * 0.55
	print("Entradas:",consumo,"kWh e tipo",tipo)
	print("Valor total: R$",round(preco,2))
elif(tipo == "C" and consumo > 1000):
	preco = consumo * 0.60
	print("Entradas:",consumo,"kWh e tipo",tipo)
	print("Valor total: R$",round(preco,2))
elif(tipo == "I" and 0<= consumo <= 5000):
	preco = consumo * 0.55
	print("Entradas:",consumo,"kWh e tipo",tipo)
	print("Valor total: R$",round(preco,2))
elif(tipo == "I" and consumo > 5000):
	preco = consumo * 0.60
	print("Entradas:",consumo,"kWh e tipo",tipo)
	print("Valor total: R$",round(preco,2))
elif(consumo < 0):
	print("Entradas:",consumo,"kWh e tipo",tipo)
	print("Dados invalidos")
else:
	print("Entradas:",consumo,"kWh e tipo",tipo)
	print("Dados invalidos")




