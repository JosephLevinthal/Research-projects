escala = input("C/F? ")

if escala == "C":
	t = float(input("temperatura: "))
	f = ((t * 9) / 5) + 32
	print(round(f, 2))
else:
	t = float(input("temperatura: "))
	c = ((t - 32) * 5) / 9
	print(round(c, 2))