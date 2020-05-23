# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código
a = float(input("consumo de energia: "))
b = input("tipo de instalacao: ").upper()
print("Entradas:",a,"kWh e tipo",b)
if (b == "R" or b == "I" or b == "C") and a>=0:
	if b == "R" and a <= 500:
		print("Valor total: R$",round(a*0.44,2))
	elif b == "R" and a > 500:
		print("Valor total: R$", round(a*0.65,2))
	elif b == "C" and a <=1000:
		print("Valor total: R$", round(a*0.55,2))
	elif b == "C" and a > 1000:
		print("Valor total: R$", round(a*0.60,2))
	elif b == "I" and a <= 5000:
		print("Valor total: R$", round(a*0.55,2))
	elif b == "I" and a > 5000:
		print("Valor total: R$", round(a*0.60,2))
else:
	print("Dados invalidos")