consumo=float(input("consumo: "))
if(consumo<=100):
	valor=consumo*1.20
	print(round(valor,2))
else:
	valor2=(consumo*1.40)+ 25.00
	print(round(valor2,2))
	