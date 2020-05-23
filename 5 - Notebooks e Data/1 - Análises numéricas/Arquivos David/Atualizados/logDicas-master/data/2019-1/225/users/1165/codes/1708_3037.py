x = float(input("Valor da funcao: "))

if (x <= -1) or (x >= 1):
	print(round(x**2, 4))
elif (-1 < x < 0) or (0 < x < 1):
	print(round(x, 4))
elif (x == 0):
	print(round(1, 4))

	
	


	