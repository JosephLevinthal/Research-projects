x = float(input("Valor de x:"))

if ((-1000) <= x < (-2) ):
	x1 = (-1/(x+2))
	print (round(x1,4))
elif (2 < x <= 1000 ):
	x1 = (1/(x-2))
	print(round(x1,4))
else:
	print("entrada invalida")
	