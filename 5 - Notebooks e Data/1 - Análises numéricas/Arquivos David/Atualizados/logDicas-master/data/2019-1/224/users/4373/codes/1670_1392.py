consumo=float(input("Digite o consumo:"))
if(consumo>10):
	c=(consumo*3.5)+30
	print(round(c,2))
else:
	d=(consumo*3.0)+30
	print(round(d,2))
