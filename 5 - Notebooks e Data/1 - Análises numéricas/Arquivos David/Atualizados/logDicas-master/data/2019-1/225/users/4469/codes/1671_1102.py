from math import*

H = float(input("H: "))
h = float(input("h: "))
r = float(input("r: "))

print("Entradas:",H,",",h,",",r)

vc = pi * (r ** 2) * (H - 2 * r)
ve = (4 / 3) * pi * (r ** 3)
vce = (pi / 3) * ((2 * r - h) ** 2) * ((3 * r) - (2 * r - h))

if(H <= 0 or h <= 0 or r <= 0 or H <= h or H < 2*r):
	print("Entradas invalidas")

elif(h < r): # semiesfera inferior
	print("Volume:", round((vce / 2) * 1000, 3), "litros")

elif((h >= r) and (h < (H - r))): # cilindro intermediário
	print("Volume:", round((vc + (vce / 2)) * 1000, 3), "litros")

elif(h >= H - 2 * r and h <= H): # semiesfera superior
	print("Volume:", round((vc + ve - vce / 2) * 1000, 3), "litros")