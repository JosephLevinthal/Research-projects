pv = int(input())
v1 = int(input())
v2 = int(input())
v3 = int(input())

n = v1 + v2 + v3
perde = pv - (10*n)

if (pv > 0) and (v1 <= 12) or (v2 <= 12) or (v3 <= 12):
	if (perde > 0):
		print(perde)
		print("VIVO")
	else:
		print(0)
		print("MORTO")
else:
	print("Entrada invalida")