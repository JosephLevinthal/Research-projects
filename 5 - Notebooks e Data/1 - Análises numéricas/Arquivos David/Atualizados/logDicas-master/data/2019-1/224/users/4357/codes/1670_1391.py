consumo=float(input("digite o numero:"))
tarifa=0.60
if (consumo<=150):
	a=(tarifa*consumo+5)
	mensagem=a 
	print(round(mensagem,2))
else:
	contrario= consumo*0.75+16
	mensagem=(contrario)
	print(round(mensagem,2))
	
	