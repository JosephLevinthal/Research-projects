x = float(input("Valor de x: "))

if ((-1000 <= x < -2) or (2 < x <= 1000)):
	if (-1000 <= x < -2):
		eq = (-1/x+2)
		print(round(eq, 4))
		else:
			eq2 = (1/x+2)
			print(round(eq2, 4))
else:
	print("entrada invalida")