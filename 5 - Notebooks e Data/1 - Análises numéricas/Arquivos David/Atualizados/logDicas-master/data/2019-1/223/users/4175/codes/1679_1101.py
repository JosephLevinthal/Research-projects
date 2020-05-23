# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("digite a quantidade de kwh gasto: "))
t = input("digite o topo de faixa de consumo: (R,I,C)")

print("Entradas: ", x,"kWh","e tipo", t.upper())

if t.upper() == "C" or t.upper() == "R" or t.upper() == "I": 
	if t.upper() == "R":
		if (x < 0):
			print("Dados invalidos")
		elif x <= 500:
			p = round((x * 0.40),2)
			print("Valor total: R$ ",p)
		else:
			p = round((x * 0.65),2)
			print("Valor total: R$ ",p)
	elif (t.upper() == "I"):
		if (x < 0):
			print("Dados invalidos")
		elif (x <= 1000):
			p = round((x * 0.55),2)
			print("Valor total: R$ ",p)
		else:
			p = round((x * 0.60),2)
			print("Valor total: R$ ",p)
	elif (t.upper() == "C"):
		if (x < 0):
			print("Dados invalidos")
		elif (x <= 5000):
			p = round((x * 0.55),2)
			print("Valor total: R$ ",p)
		else:
			p = round((x * 0.60),2)
			print("Valor total: R$ ",p)
			
else:
	print("Dados invalidos")
