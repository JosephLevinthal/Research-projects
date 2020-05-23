x = float(input("consumo de energia: "))

if(x >= 0) and (x <= 150):
	tarifa = 0.60
	taxa = 5
	valor = (x * tarifa) + taxa
	print(round(valor,2))
elif(x > 150) and (x <= 250):
	tarifa = 0.65
	taxa = 8
	valor = (x * tarifa) + taxa
	print(round(valor,2))
elif(x > 250) and (x <= 350):
	tarifa = 0.70
	taxa = 12
	valor = (x * tarifa) + taxa
	print(round(valor,2))
elif(x > 350):
	tarifa = 0.75
	taxa = 16
	valor = (x * tarifa) + taxa
	print(round(valor,2))

	
	
	
	
	
	
	
	