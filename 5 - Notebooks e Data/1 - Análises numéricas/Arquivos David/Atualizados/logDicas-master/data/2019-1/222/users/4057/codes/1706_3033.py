x = float(input("Qual o valor de x: "))

if (-100 <= x) and (x < 0):
	a = -(1/x)
	print(round(a, 4))
elif (0 < x) and (x <= 100):
	a = (1/x)
	print(round(a, 4))
else :
	print("entrada invalida")