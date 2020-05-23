# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a=float(input("consumo de energia: "))
b=input("tipo de instacao: ").upper()
print("Entradas: " , a, "kWh e tipo", b)

if(a >= 0):
	if(b == "R"):	
		if(a <= 500):
			s = a * 0.44
			print("Valor total: R$", round(s, 2))
		else:
			s = a * 0.65
			print("Valor total: R$", round(s, 2))
	if(b == "C"):
		if(a <= 1000):
			s = a * 0.55
			print("Valor total: R$", round(s, 2))
		else:
			s = a * 0.60
			print("Valor total: R$", round(s, 2))
	if(b == "I"):
		if(a <= 5000):
			s = a * 0.55
			print("Valor total: R$", round(s, 2))
		else:
			s = a * 0.60
			print("Valor total: R$", round(s, 2))	
else:
	print("Dados invalidos")

