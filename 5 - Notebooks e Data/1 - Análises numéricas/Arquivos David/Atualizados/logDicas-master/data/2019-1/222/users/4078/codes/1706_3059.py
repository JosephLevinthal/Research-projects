x = float(input("consumo de minutos: "))



if(x >= 0) and (x <= 100):
	tarifa = 1.20
	taxa = 1
	valor = (x * tarifa) + taxa
	print(round(valor,2))
elif(x > 0) and (x <= 200):
	tarifa = 1.30
	taxa = 10
	valor = (x * tarifa) + taxa
	print(round(valor,2))
elif(x > 200) and (x <= 300):
   tarifa = 1.40
	taxa  = 20
	valor = (x * tarifa) + taxa
	print(round(valor,2))
elif(x > 300):
	tarifa = 1.50
	taxa = 25
	valor = (x * tarifa) + taxa
	print(round(valor,2))