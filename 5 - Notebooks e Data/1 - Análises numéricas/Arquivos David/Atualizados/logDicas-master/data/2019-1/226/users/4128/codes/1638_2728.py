p = float(input("percurso:"))
car = (input("tipo (A/B)"))

cara = 8
carb = 12

if(car.upper() == ("A")):
	c = p/cara
	print(round(c, 2))
else:
	c = p/carb
	print(round(c, 2))