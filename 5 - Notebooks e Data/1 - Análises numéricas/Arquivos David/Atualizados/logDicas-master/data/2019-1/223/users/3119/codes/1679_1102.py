from math import*

H = float(input("Digite a altura: "))
h = float(input("Digite o nivel de combustivel: "))
r = float(input("Digite o raio: "))


print("Entradas:",H,",",h,",",r)

v = (4/6)*pi*(r**3)
vt = (4/3)*pi*(r**3) + pi*(H - 2*r)*(r**2)
calota = (pi*((H - h)**2)*((3*r)-(H - h)))/3

if(H > 0 and h > 0 and r > 0 and H > h and H > (2*r)):
	if(h < r):
		vol = v * 1000
		print("Volume:",round(vol,3),"litros")
	elif((h >= r) and (h < (H -r))):
		vol = (v + (pi * (h - r)*(r**2)))*1000
		print("Volume:",round(vol,3),"litros")
	elif(h >= (H - r)):
		vol = (vt - calota) *1000
		print("Volume:",round(vol,3),"litros")
else:
	print("Entradas invalidas")
	
