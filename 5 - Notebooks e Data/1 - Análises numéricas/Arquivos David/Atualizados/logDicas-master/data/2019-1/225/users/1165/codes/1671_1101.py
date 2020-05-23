tipo = input("Tipo de instalacao (R, I ou C): ").upper()
faixa = float(input("Faixa de consumo: "))

print("Entradas: ", faixa, "kWh e tipo", tipo)
if (faixa > 0 and tipo == "R" or tipo == "I" or tipo == "C"):
	if (tipo == "R"):
		if (faixa <= 500):
			preco = faixa * 0.44
			print("Valor total: R$", round(preco, 2))
		else:
			preco = faixa * 0.65
			print("Valor total: R$", round(preco, 2))
	elif (tipo == "C"):
		if (faixa <= 1000):
			preco = faixa * 0.55
			print("Valor total: R$", round(preco, 2))
		else:
			preco = faixa * 0.60
			print("Valor total: R$", round(preco, 2))
	elif (tipo == "I"):
		if (faixa <= 5000):
			preco = faixa * 0.55
			print("Valor total: R$", round(preco, 2))
		else:
			preco = faixa * 0.60
			print("Valor total: R$", round(preco, 2))
else:
	print("Dados invalidos")
