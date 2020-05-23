# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
c = float(input())
t = input()
if(c<=500 and t=="R"):
	total = c *0.44
	print("Entradas: ", c, "kWh e tipo", t)
	print("Valor total: R$", round(total, 2))
elif(c>500 and t=="R"):
	total = c *0.65
	print("Entradas: ", c, "kWh e tipo", t)
	print("Valor total: R$", round(total, 2))
elif(c<=1000 and t=="C"):
	total = c *0.55
	print("Entradas: ", c, "kWh e tipo", t)
	print("Valor total: R$", round(total, 2))
elif(c>1000 and t=="C"):
	total = c *0.60
	print("Entradas: ", c, "kWh e tipo", t)
	print("Valor total: R$", round(total, 2))
elif(c<=5000 and t=="i"):
	total = c *0.55
	print("Entradas: ", c, "kWh e tipo", t)
	print("Valor total: R$", round(total, 2))
elif(c>5000 and t=="i"):
	total = c *0.60
	print("Entradas: ", c, "kWh e tipo", t)
	print("Valor total: R$", round(total, 2))
else:
	print("Entradas: ", c, "kWh e tipo", t)
	print("Dados invalidos")