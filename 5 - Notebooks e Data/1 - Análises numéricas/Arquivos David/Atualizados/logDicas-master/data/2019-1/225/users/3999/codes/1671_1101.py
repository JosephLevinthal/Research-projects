# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=float(input("Consumo:"))
y=input("Instalacao:").upper()
print("Entradas:",x,"kWh e tipo",y)
if((y!="C")and(y!="R")and(y!="I"))or(x<0):
	z="Dados invalidos"
	print(z)
elif (y=="R"):
	if(x<=500):
	   z= x*0.44
		print("Valor total:R$",round(z,2))
	else:
		z=x*0.65
		print("Valor total: R$",round(z,2))
elif (y=="C"):
		if(x<=1000):
		z=x*0.55		
		print("Valor total: R$",round(z,2))
		else:	
		z=x*0.60
		print("Valor total: R$",round(z,2))
elif(y=="I"):
		if(x<=5000):
		z=x*0.55
		print("Valor total: R$",round(z,2))
		else:
		z=x*0.6
		print("Valor total: R$",round(z,2))


		
			