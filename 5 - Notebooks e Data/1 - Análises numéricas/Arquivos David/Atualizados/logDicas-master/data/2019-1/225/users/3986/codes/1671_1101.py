# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
c=float(input("consumo/h:"))
t=input("Qual o tipo? R/C/I")
print("Entradas:",c,"kWh e tipo",t)
		  
if(c<0 or (not(t=="R" or t=="C" or t=="I"))):
	h="Dados invalidos"
	print(h)
else:
	if((c<=500 and t=="R")or(c<=1000 and t=="C")or(c<=5000 and t=="I")):
		if(t=="R"):
			h=round((c*0.44), 2)
			print("Valor total: R$",h)
		elif(t=="C"):
			h=round((c*0.55), 2)
			print("Valor total: R$ ",h)
		else:
			h=round((c*0.55), 2)
			print("Valor total: R$ ",h)
	else:
		if(t=="R"):
			h=round((c*0.65), 2)
			print("Valor total: R$ ",h)
		elif(t=="C"):
			h=round((c*0.60), 2)
			print("Valor total: R$ ",h)
		else:
			h=round((c*0.60), 2)
			print("Valor total: R$ ",h)