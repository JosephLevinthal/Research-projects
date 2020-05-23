num = int(input("Numero de aproximacao: "))

cont = 1
ap = 3
while (cont < num):
	den = (cont * 2) * (cont * 2 + 1) * (cont * 2 + 2)
	ap = ap + (-1)** (cont + 1) * 4 / den
	cont = cont + 1
print(round(ap, 8))