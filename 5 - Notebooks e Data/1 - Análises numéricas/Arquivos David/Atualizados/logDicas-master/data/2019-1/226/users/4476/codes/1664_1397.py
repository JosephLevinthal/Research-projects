area = float(input("area a ser fertilizada: "))

if ( area <= 10000):
	custo = 5*area
	print(round(custo, 2))
	
else:
	custo = (5*10000) + 4*(area - 10000)
	print(round(custo, 2))