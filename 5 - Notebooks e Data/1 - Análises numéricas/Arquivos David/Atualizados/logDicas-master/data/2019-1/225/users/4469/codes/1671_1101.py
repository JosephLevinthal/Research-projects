# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
consumo = float(input())
tipo = input().upper()

print("Entradas: " + str(consumo) + " kWh e tipo " + tipo)

if(consumo > 0 and (tipo == "R" or tipo == "I" or tipo == "C")):
	if(tipo == "R"):
		if(consumo <= 500.0):
			print("Valor total: R$ " + str(round(consumo * 0.44, 2)))
		else:
			print("Valor total: R$ " + str(round(consumo * 0.65, 2)))
	elif(tipo == "I"):
		if(consumo <= 5000.0):
			print("Valor total: R$ " + str(round(consumo * 0.55, 2)))
		else:
			print("Valor total: R$ " + str(round(consumo * 0.60, 2)))
	else:
		if(consumo <= 1000.0):
			print("Valor total: R$ " + str(round(consumo * 0.55, 2)))
		else:
			print("Valor total: R$ " + str(round(consumo * 0.60, 2)))
else:
	print("Dados invalidos")