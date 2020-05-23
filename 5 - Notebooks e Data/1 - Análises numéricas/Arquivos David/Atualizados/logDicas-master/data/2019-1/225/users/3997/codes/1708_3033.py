x = float(input("Digite x: "))

if (-100 <= x) and (x < 0):
	print(round((-1/x),4))
elif (0 < x) and (x <= 100):
	print(round((1/x),4))
else:
	print("entrada invalida")
