consumo = float(input("digite o valor:"))
tipo = input("digite o tipo: r, i ou c").upper()

residencial = round(consumo*(0.44), 2)
residencial1 = round(consumo*(0.65), 2)
comercial = round(consumo*(0.55), 2)
comercial1 = round(consumo*(0.60), 2)
industrial = round(consumo*(0.55), 2)
industrial1 = round(consumo*(0.60), 2)
print("Entradas:", consumo, "kWh e tipo", tipo)

if(consumo>0):
	if(tipo=="R") and (consumo<=500):
		print("Valor total:", "R$", residencial)
	elif(tipo=="R") and (consumo>500):
		print("Valor total:", "R$", residencial1)
	elif(tipo=="C") and (consumo<=1000):
		print("Valor total:", "R$", comercial)
	elif(tipo=="C") and (consumo>1000):
		print("Valor total:", "R$", comercial1)
	elif(tipo=="I") and (consumo<=5000):
		print("Valor total:", "R$", industrial)
	elif(tipo=="I") and (consumo>5000):
		print("Valor total:", "R$", industrial1)
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")
	