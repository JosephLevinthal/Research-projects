# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
c=float(input("Qual o consumo: "))
ti=input("Qual o tipo de instalacao: R, C ou I: ")
preco=0
if (c <= 0) or (not(ti == "R") and not (ti == "C") and not (ti == "I")):
	print("Entradas:", c, "kWh e tipo", ti)
	print("Dados invalidos")
elif (ti=="R"):
	if (c <= 500):
		preco=0.44
	else:
		preco=0.65
elif (ti=="C"):
	if (c <= 1000):
		preco=0.55
	else:
		preco=0.60
elif (ti=="I"):
	if (c <= 5000):
		preco=0.55
	else:
		preco=0.60
if (preco > 0):
	print("Entradas:", c, "kWh e tipo", ti)
	print("Valor total: R$", round(preco*c,2))