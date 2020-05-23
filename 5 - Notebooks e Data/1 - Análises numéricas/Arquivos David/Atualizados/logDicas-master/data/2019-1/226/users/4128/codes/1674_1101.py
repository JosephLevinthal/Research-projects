# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

x = float(input("Consumo de energia:"))
y = input("Tipo de instalacao:").upper()

if(x < 0):
	print("Entradas:",x, "kWh e tipo",y)
	print("Dados invalidos")
elif((x <= 500) and (y == "R")):
	v = x * 0.44
	z = round(v,2)
	print("Entradas:",x, "kWh e tipo",y)
	print("Valor total: R$",z)
elif((x > 500) and (y == "R")):
	v = x * 0.65
	z = round(v,2)
	print("Entradas:",x, "kWh e tipo",y)
	print("Valor total: R$",z)
elif((x <= 1000) and (y == "C")):
	v = x * 0.55
	z = round(v,2)
	print("Entradas:",x, "kWh e tipo",y)
	print("Valor total: R$",z)
elif((x > 1000) and (y == "C")):
	v = x * 0.60
	z = round(v,2)
	print("Entradas:",x, "kWh e tipo",y)
	print("Valor total: R$",z)
elif(x <= 5000 )and ((y == "I")):
	v = x * 0.55
	z = round(v,2)
	print("Entradas:",x, "kWh e tipo",y)
	print("Valor total: R$",z)
elif((x > 5000 )and (y == "I")):
	v = x * 0.60
	z = round(v,2)
	print("Entradas:",x, "kWh e tipo",y)
	print("Valor total: R$",z)
else:
	print("Entradas:",x, "kWh e tipo",y)
	print("Dados invalidos")
	