p = float(input(" digite o percurso "))
t = input(" A/B?")
if(t == "A"):
	consumo = float(p/8)
	print(round(consumo,2))
else:
	consumo = float(p/12)
	print(round(consumo,2))
	
