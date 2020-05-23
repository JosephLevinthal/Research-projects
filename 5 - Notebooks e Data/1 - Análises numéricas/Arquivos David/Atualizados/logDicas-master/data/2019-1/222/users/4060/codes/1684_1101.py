# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=float(input("Entrada x: "))
y=input("Entrada y: ")
print("Entradas:", x , "kWh e tipo", y)
if((x<0)or(y!="R")and(y!="I")and(y!="C")):
	print("Dados invalidos")
elif((x<=500)and(y=="R")):
	print("Valor total: R$", round(x*0.44, 2))
elif((x>500)and(y=="R")):
	print("Valor total: R$", round(x*0.65, 2))
elif((x<=1000)and(y=="C")):
	print("Valor total: R$", round(x*0.55, 2))
elif((x>1000)and(y=="C")):
	print("Valor total: R$", round(x*0.60, 2))
elif((x<=5000)and(y=="I")):
	print("Valor total: R$", round(x*0.55, 2))
elif((x>5000)and(y=="I")):
	print("Valor total: R$", round(x*0.60, 2))	
