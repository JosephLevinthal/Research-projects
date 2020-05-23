escala = input("insira a escala em F/C: ")
T = int(input("Valor da temperatura:" ))

C = 5/9 * (T - 32)
F = (9 * T)/5 + 32

if (escala == "C"):
	print(round(F,2))
else:
	print(round(C,2))