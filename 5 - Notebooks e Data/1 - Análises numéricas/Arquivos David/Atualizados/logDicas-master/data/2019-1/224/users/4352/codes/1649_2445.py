escala = (input("digite a escala: (C/F)"))
valor = float(input("digite a temperatura: "))
formula1 = 5/9 * (valor - 32)
formula2 = 9*valor/5 + 32
if escala == "F":
	print(round(formula1, 2))
else:
	print(round(formula2, 2))

