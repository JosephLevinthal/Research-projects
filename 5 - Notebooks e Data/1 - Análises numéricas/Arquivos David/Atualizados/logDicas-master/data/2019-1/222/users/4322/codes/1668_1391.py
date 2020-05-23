consumo = float(input("quanto consumiu? "))
resultado = consumo * 0.60 + 5
resultado2 = consumo * 0.75 + 16
if (consumo <= 150):
	print(resultado)
else:
	print(resultado2)