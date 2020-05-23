g = float(input("Peso da encomenda em gramas: "))

if (g >= 5000.0):
	x = ((g*0.04) + 60)
	
	print(round(x, 2))
else: 
	x = (g*0.05)
	
	print(round(x, 2))