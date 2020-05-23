consumo=float(input("consumo de energia em kwh: "))
tipo=input("tipo de instalacao R ou I ou C: ")
tipo=tipo.upper()
print("Entradas: ",consumo,"kWh", " e tipo",tipo.upper())
if (tipo== "R") and (consumo>0) and (consumo<=500):
	total= consumo*0.44
	print("Valor total: R$",round(total, 2))
elif (tipo== "R") and (consumo>0) and (consumo>500):
	total= consumo*0.65
	print("Valor total: R$",round(total, 2))
elif (tipo=="C") and (consumo>0) and (consumo<=1000):
	total= consumo*0.55
	print("Valor total: R$",round(total, 2))
elif (tipo=="C") and (consumo>0) and (consumo>1000):
	total= consumo*0.60
	print("Valor total: R$",round(total, 2))
elif (tipo=="I") and (consumo>0) and (consumo<=5000):
	total=consumo*0.55
	print("Valor total: R$",round(total, 2))
elif (tipo=="I") and (consumo>0) and (consumo>5000):
	total=consumo*0.60
	print("Valor total: R$",round(total, 2))
else:
	print("Dados invalidos")
	
