from math import*
H = float(input("Altura total do tanque: "))
h = float(input("Nivel de combustivel do tanque: "))
r = float(input("Raio: "))

print("Entradas: {} , {} , {}".format(H,h,r))


# Verificar se as entradas são válidas
if (H < 0) or (h < 0) or (r < 0) or (H < h) or (H < 2*r):
	print("Entradas invalidas")
else:
	if (h < r): #Caso 1
		V=(1/3)*pi*(h**2)*(3*r - h)
	elif (h < H - r): #Caso 2
		V=(2/3)*pi*r**3 + pi*r**2*(h - r)
	elif (h <= H): #Caso 3
		V=(4/3)*pi*(r**3) + pi*(r**2)*(H - 2*r) - (1/3)*pi*((H-h)**2) * (3*r - (H-h))
	
	print("Volume:",round(V*1000,3),"litros")