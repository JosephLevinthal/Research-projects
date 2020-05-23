p = float(input("percurso: "))
tp = input("tipo do carro (A/B) ")

if (tp.upper() == "A" ):
	x = p/8
	print(float(round(x, 2)))
	
else:
	x = p/12
	print(float(round(x, 2)))

