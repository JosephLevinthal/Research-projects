consumo=float(input());
tipo=input().upper();
print("Entradas: ",consumo, "kWh e tipo",tipo)
if(tipo=="R" or tipo=="I" or tipo=="C") and(consumo>0):
	if(tipo=="R"):
		if(consumo<=500):
			a=consumo*0.44
			print("Valor total: R$ ",round(a,2))
		else:
			a=consumo*0.65
			print("Valor total: R$ ",round(a,2))
	elif(tipo=="C"):
		if(consumo<=1000):
			a=consumo*0.55
			print("Valor total: R$ ",round(a,2))
		else:
			a=consumo*0.60
			print("Valor total: R$ ",round(a,2))
	else:
		if(consumo<=5000):
			a=consumo*0.55
			print("Valor total: R$ ",round(a,2))
		else:
			a=consumo*0.60
			print("Valor total: R$ ",round(a,2))
else:
	print("Dados invalidos")
		