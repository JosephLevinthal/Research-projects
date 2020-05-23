e = input("Qual e a escala esta representada(C/F)? ")
t = int(input("Qual e a temperatura? "))

if (e == "C"):
	F = (1.8 * t) + 32
	print(round(F, 2))
else:
	C = (5 / 9) * (t- 32)
	print(round(C, 2))