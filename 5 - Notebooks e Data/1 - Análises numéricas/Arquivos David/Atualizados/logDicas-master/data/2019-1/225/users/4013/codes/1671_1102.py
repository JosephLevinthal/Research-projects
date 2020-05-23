H = float(input("altura total do tanque:"))
h = float(input("nivel de combustivel na tanque:"))
r = float(input("raio dos bojos semiesfericos inferior e superior:"))
print ("Entradas:" , H , "," , h , "," , r)

from math import*
#volume da calota
if ((H >0) and(h >0) and (r >0) and (H >h) and (H > 2 * r)):
	if (h == r):
		vol = ((4/3)* pi *(r ** 3))/ 2
		print("Volume:" , (round(vol * 1000), 3), "litors")
	elif (h < r):
		vol = (pi/3) * (h ** 2) * (3 * r - h)
		print("Volume:", (vol *1000), "litros")
#volume da esfera e do cilindro
	elif(h == H - r):
		vol = round(((pi * (r ** 2) * (H - 2* r)) + (2/3) * pi *(r ** 3)) , 3)
		print("Volume:" , (vol * 1000) , "litros")
	elif((h < H - r)and (h > r)):
		vol = pi * (r ** 2)* (h - r) + ((4/3) * pi * (r **3)) / 2
		print("Volume:", round((vol * 1000), 3), "litros")
	else:
		vol = pi * (r**2) * (H - 2 * r) + 4 /3 * pi * (r**3) - (pi / 3) * ((H-h)**2) * (3*r - (H - h))
		print("Volume:", round((vol * 1000), 3), "litros")
else:
	print("Entradas invalidas")