x = int(input("PO: "))
y = input("Armadura: ").upper()
d = int(input("Dado:(1/8) "))

a = "INTEIRA"
b = "MALHA"
c = "PLACA"

if d > 8 or d < 1 or (y != a) and (y != b) and (y != c):
	print("Entrada invalida")
elif y == a:
	if x >= 200:
		r = (30 * d) - 20
		print(r)
	else:
		print("PO insuficiente")
elif y == c:
	if x >= 100:
		r = (20 * d) - 18
		print(r)
	else:
		print("PO insuficiente")
else:
	if x >= 50:
		r = (15 * d) - 1
		print(r)
	else:
		print("PO insuficiente")