m = int(input("minutos no telefone: "))
a = m * 1.20
b = 25 + (m * 1.40)
if (m <= 100):
	print(round(a, 2))
else:
	print(round(b, 2))