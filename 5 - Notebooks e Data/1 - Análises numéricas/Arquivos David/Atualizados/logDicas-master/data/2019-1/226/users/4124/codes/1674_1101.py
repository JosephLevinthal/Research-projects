# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("Consumo em kWh: "))
y = input("Tipo de instalacao: ")
y = y.upper()
print("Entradas:", x ,"kWh e tipo", y,)
if(y != "R" and y != "I" and y != "C" or x < 0):
	print("Dados invalidos")
elif(y == "R" and x <= 500):
	a = x * 0.44
	a = round(a,2)
	print("Valor total: R$", a)
elif(y == "R" and x > 500):
	a = x * 0.65
	a = round(a,2)
	print("Valor total: R$", a)
elif(y == "C" and x <= 1000):
	a = x * 0.55
	a = round(a,2)
	print("Valor total: R$", a)
elif(y == "C" and x > 1000):
	a = x * 0.60
	a = round(a,2)
	print("Valor total: R$", a)
elif(y == "I" and x <= 5000):
	a = x * 0.55
	a = round(a,2)
	print("Valor total: R$", a)
elif(y == "I" and x > 5000):
	a = x * 0.60
	a = round(a,2)
	print("Valor total: R$", a)

	
	
	