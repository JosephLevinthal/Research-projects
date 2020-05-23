# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("Insira o consumo de energia: "))
y = input("Insira o tipo de intalacao: ").upper()

print("Entradas:", x, "kWh e tipo", y)

if((y != "R") and (y != "I") and (y != "C") or (x < 0 )):
	print("Dados invalidos")
elif((y == "R") and (x <= 500)):
	v = x * 0.44
	V = round(v, 2)
	print("Valor total: R$", V)
elif((y == "R") and (x > 500)):
	v = x * 0.65
	V = round(v, 2)
	print("Valor total: R$", V)
elif((y == "C") and (x <= 1000)):
	v = x * 0.55
	V = round(v, 2)
	print("Valor total: R$", V)
elif((y == "C") and (x > 1000)):
	v = x * 0.60
	V = round(v, 2)
	print("Valor total: R$", V)
elif((y == "I") and (x <= 5000)):
	v = x * 0.55
	V = round(v, 2)
	print("Valor total: R$", V)
elif((y == "I") and (x > 5000)):
	v = x * 0.60
	V = round(v, 2)
	print("Valor total: R$", V)