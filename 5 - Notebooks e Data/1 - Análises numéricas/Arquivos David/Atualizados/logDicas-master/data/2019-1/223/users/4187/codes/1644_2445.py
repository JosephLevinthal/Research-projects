escala = input("escala de temperatura: (C/F)" )
graus = float(input("graus a ser convertido:"))

if escala == 'F':
	C = (5/9) * (graus - 32)
	print(round(C,2))

else:
	F = (9 * graus) / 5 + 32
	print(round(F,2))
