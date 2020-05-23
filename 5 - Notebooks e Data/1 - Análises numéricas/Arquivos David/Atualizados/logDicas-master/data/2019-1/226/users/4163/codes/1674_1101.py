# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("consumo de energia: "))
y = input("tipo de instalacao: ").upper()

print("Entradas:",x,"kWh e tipo",y)

if (x>=0) and(x<=500)and(y == "R"):
	p = round(x * 0.44, 2)
	print("Valor total: R$",p)
elif (x>=0) and(x>500)and(y == "R"):
	p = round(x * 0.65, 2)
	print("Valor total: R$",p)
elif (x>=0) and(x<=1000)and(y == "C"):
	p = round(x * 0.55, 2)
	print("Valor total: R$",p)
elif (x>=0) and(x>1000)and(y == "C"):
	p = round(x * 0.60, 2)
	print("Valor total: R$",p)
elif (x>=0) and(x<=5000)and(y == "I"):
	p = round(x * 0.55, 2)
	print("Valor total: R$",p)
elif (x>=0) and(x>5000)and(y == "I"):
	p = round(x *0.60, 2)
	print("Valor total: R$",p)
else:
	print("Dados invalidos")