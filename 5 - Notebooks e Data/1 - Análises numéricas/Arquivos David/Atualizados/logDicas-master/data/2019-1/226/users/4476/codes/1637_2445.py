escala = input("qual escala? (C/F) ")
vt = float(input("valor da temperatura: "))


if (escala.upper() == "F" ):
	c = (5*(vt-32)) / 9
	print(round(c, 2))
	
else: 
	f = (vt*9/5) + 32
	print(round(f, 2))