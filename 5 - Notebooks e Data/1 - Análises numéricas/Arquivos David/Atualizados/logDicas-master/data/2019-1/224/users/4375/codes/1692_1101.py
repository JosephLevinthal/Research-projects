consumo=float(input("consumo de energia: "))
tipo=input("instalacao R, I ou C: ")
print("Entradas:",consumo, "kWh e tipo", tipo.upper())
tipo=tipo.upper()
if(tipo=="R") and (consumo>0) and (consumo<=500):
	msg= consumo*0.44
	print("Valor total: R$",round(msg,2))
elif(tipo=="R") and (consumo>0) and (consumo>500):
	msg= consumo*0.65
	print("Valor total: R$",round(msg,2))
elif(tipo=="C") and (consumo>0) and (consumo<=1000):
	msg= consumo*0.55
	print("Valor total: R$",round(msg,2))
elif(tipo=="C") and (consumo>0) and (consumo>1000):
	msg= consumo*0.60
	print("Valor total: R$",round(msg,2))
elif(tipo=="I") and (consumo>0) and (consumo<=5000):
	msg= consumo*0.55
	print("Valor total: R$",round(msg,2))
elif(tipo=="I") and (consumo>0) and (consumo>5000):
	msg= consumo*0.60
	print("Valor total: R$",round(msg,2))
else:
	print("Dados invalidos")
	
	
	
