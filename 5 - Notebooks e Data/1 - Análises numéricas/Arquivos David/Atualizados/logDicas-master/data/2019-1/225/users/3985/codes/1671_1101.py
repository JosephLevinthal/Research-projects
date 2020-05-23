# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x= float(input("Consumo de energia: "))
v= input("Tipo de instalacao: (R,I,C)?")

print("Entradas: ", x,"kWh e tipo",v)

if (x<0) and (v != "R","I","C"):
	print("Dados invalidos")
elif (v=="R") and (x<=500):
	g= (x*0.44)
	f= round(g, 2)
	print("Valor total: R$", f)
elif (v=="R") and (x>500):
	g= (x*0.65)
	f= round(g, 2)
	print("Valor total: R$", f)
elif (v=="I") and (x<=1000):
	g= (x*0.55)
	f= round(g, 2)
	print("Valor total: R$", f)
elif (v=="I") and (x>1000):
	g= (x*0.60)
	f= round(g, 2)
	print("Valor total: R$", f)
elif (v=="C") and (x<=5000):
	g= (x*0.55)
	f= round(g, 2)
	print("Valor total: R$", f)
elif (v=="C") and (x>5000):
	g= (x*0.60)
	f= round(g, 2)
	print("Valor total: R$", f)