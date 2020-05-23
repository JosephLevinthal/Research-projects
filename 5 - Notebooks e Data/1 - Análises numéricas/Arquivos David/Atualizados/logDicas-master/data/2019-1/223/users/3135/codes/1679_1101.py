# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
c= float(input("Insira o consumo de energia:"))
t= input("Insira o tipo de instalacao:").upper()


if (t=="R" and c<= 500 and c>0):
	print("Entradas:",c,"kWh e tipo",t)
	print("Valor total: R$", round(c* 0.44,2) )
elif (t=="R" and c> 500 and c>0):
	print("Entradas:",c,"kWh e tipo",t)
	print("Valor total: R$", round(c* 0.65,2) )
elif (t=="C" and c<= 1000 and c>0):
	print("Entradas:",c,"kWh e tipo",t)
	print("Valor total: R$", round(c* 0.55,2) )
elif (t=="C" and c>1000 and c>0):
	print("Entradas:",c,"kWh e tipo",t)
	print("Valor total: R$", round(c* 0.60,2) )
elif (t=="I" and c<= 5000 and c>0):
	print("Entradas:",c,"kWh e tipo",t)
	print("Valor total: R$", round(c* 0.55,2))
elif (t=="I" and c> 5000 and c>0):
	print("Entradas:",c,"kWh e tipo",t)
	print("Valor total: R$", round(c* 0.60,2))

else:
	print("Entradas:",c,"kWh e tipo",t)
	print("Dados invalidos")
	