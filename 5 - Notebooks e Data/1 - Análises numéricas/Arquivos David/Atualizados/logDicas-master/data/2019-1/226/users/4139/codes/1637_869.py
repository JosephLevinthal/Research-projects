vc = float(input("valor total de compras:"))

if (vc >= 200):
	x = (vc-(vc*0.05))
else:
	x = vc

print(round(x,2))