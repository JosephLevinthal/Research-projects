# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
consumo = float(input("Consumo: "))
tipo = input("Tipo de instalacao: ").upper()

print("Entradas:", consumo, "kWh e tipo", tipo)
if (consumo < 0 or tipo != "R" and tipo != "C" and tipo != "I"):
	print("Dados invalidos")
	
else:
	if (tipo == "R"):
		if (consumo <= 500):
			preco = 0.44

		else:
			preco = 0.65

	elif (tipo == "C"):
		if (consumo <= 1000):
			preco = 0.55

		else:
			preco = 0.60

	elif (tipo == "I"):
		if (consumo <= 5000):
			preco = 0.55

		else:
			preco = 0.60
	valor = consumo*preco
	print("Valor total: R$",round(valor,2))