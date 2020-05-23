x=float(input("Qual o valor de x?: "))
if (x == 2 or x == -2 or x > 1000 or x < -1000):
	print("entrada invalida")
elif (x > 2 and x <= 1000):
	print(round(1/(x-2),4))
elif (x >= -1000 and x < -2):
	print(round(-1/(x+2),4))