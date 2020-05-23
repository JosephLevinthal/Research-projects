# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
cons = float(input("Digite aqui o consumo de energia: "))
inst = input("Digite aqui o tipo de instalacao: ").upper()
print("Entradas:", cons, "kWh", "e", "tipo", inst)
x1 = cons * 0.44
x2 = cons * 0.65
y1 = cons * 0.55
y2 = cons * 0.60
if ((inst == "R") and (cons > 0)):
	if (cons <= 500):
		print("Valor total: R$", round(x1, 2))
	else:
		print("Valor total: R$", round(x2, 2))
elif ((inst == "C") and (cons > 0)):
	if (cons <= 1000):
		print("Valor total: R$", round(y1, 2))
	else:
		print("Valor total: R$", round(y2, 2))
elif ((inst == "I") and (cons > 0)):
	if (cons <= 5000):
		print("Valor total: R$", round(y1, 2))
	else:
		print("Valor total: R$", round(y2, 2))
else:
	print("Dados invalidos")