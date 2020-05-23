# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("Digite o consumo de energia: "))
y = input("Digite o tipo de instalacao (R/I/C)?: ")
print("Entradas:",x,"kWh","e tipo",y)
if((x>0)and(y=="R")):
	if(x<=500):
		z = 0.44*x
		print("Valor total: R$",round(z,2))
	else:
		z = 0.65*x
		print("Valor total: R$",round(z,2))
elif((x>0)and(y=="C")):
	if(x<=1000):
		z = 0.55*x
		print("Valor total: R$",round(z,2))
	else:
		z = 0.60*x
		print("Valor total: R$",round(z,2))
elif((x>0)and(y=="I")):
	if(x<=5000):
		z = 0.55*x
		print("Valor total: R$",round(z,2))
	else:
		z = 0.60*x
else:
	print("Dados invalidos")
		
		
		