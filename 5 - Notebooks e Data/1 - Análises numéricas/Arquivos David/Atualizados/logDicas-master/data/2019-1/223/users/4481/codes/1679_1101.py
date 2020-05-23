# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
c=float(input("consumo de energia: "))
a=input("tipo de instalacao: ").upper()
print("Entradas:",c,"kWh e tipo",a)
if (c>=0):
	if(a=="R") :
		if(c<=500):
			p=c*0.44
			print("Valor total: R$",round(p,2))
		else:
			p=c*0.65
			print("Valor total: R$",round(p,2))
	elif(a=="C"):
		if(c<=1000):
			p=c*0.55
			print("Valor total: R$",round(p,2))
		else:
			p=c*0.6
			print("Valor total: R$",round(p,2))
	elif(a=="I"):
		if(c<=5000):
			p=c*0.55
			print("Valor total: R$",round(p,2))
		else:
			p=c*0.6
			print("Valor total: R$",round(p,2))
	else:
		print("Dados invalidos")				
else:
	print("Dados invalidos")