peso=float(input())

if (peso<5000):
	valor=peso*(5/100)
	print(round(valor,2))
else:
	valor=peso*(4/100) + 60
	print(round(valor,2))
	