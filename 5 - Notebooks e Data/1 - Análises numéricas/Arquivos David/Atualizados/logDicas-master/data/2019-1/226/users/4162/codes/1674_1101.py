ce= float(input("insira o consumo de energia (em kWh): "))
ti= input("tipo de instalacao (R para residencias, I para industrias, e C para comercios): ").upper()
print("Entradas:",ce,"kWh","e tipo",ti)
if (ce>0) and ((ti=="R")or(ti=="I")or(ti=="C")):
	if (ce<=500)and(ti=="R"):
		print("Valor total: R$",round((0.44*ce),2))
	elif (ce>500)and(ti=="R"):
		print("Valor total: R$",round((0.65*ce),2))
	elif (ce<=1000)and(ti=="C"):
		print("Valor total: R$",round((0.55*ce),2))
	elif (ce>1000)and(ti=="C"):
		print("Valor total: R$",round((0.60*ce),2))
	elif (ce<=5000)and(ti=="I"):
		print("Valor total: R$",(0.55*ce))
	elif (ce>5000)and(ti=="I"):
		print("Valor total: R$",(0.60*ce))
else:
	print("Dados invalidos")