# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("consumo de energia: "))
y = input("tipo de instalacao: ")
print("Entradas:",x,"kWh e tipo",y )             

if(y == "R"):
	if((x > 0) and (x < 500)):
		print("Valor total: R$",round(x * 0.44,2))
	elif((x > 500)):
		print("Valor total: R$",round(x * 0.65,2))
elif(y == "C"):
	if((x > 0) and (x < 1000)):
		print("Valor total: R$",round(x * 0.55,2))
	elif(x > 1000):
		print("Valor total: R$",round(x * 0.60,2))
if(y == "I"):
	if(x > 0) and (x < 5000):
		print("Valor total: R$",round(x * 0.55,2))
	elif(x > 5000):
		print("Valor total: R$",round(x * 0.60,2))

	else:
		print("Dados invalidos")
