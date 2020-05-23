H = float(input("digite H: "))
h = float(input("digite h: "))
r = float(input("digite r: "))
print("Entradas:", H, ",", h, ",", r)

from math import*

if ((H>0) and (h>0) and (r>0) and (H>h) and (H>2*r)):
	if (h==r):
		vol = ((4/3) * pi *(r ** 3))/ 2
		print("Volume:", (round((vol * 1000), 3)), "litros")
	elif (h < r):
		vol = (pi / 3) * (h ** 2) * (3 * r - h)
		print("Volume:",(vol * 1000), "litros")
	elif (h == H - r):
		vol = round(((pi * (r ** 2) * (H - 2 *r)) + (2 / 3) *  pi * (r ** 3)), 3)
		print("Volume:", (round((vol * 1000), 3)), "litros")
	elif(h<H-r and h>r):
		vol = pi * (r ** 2) * (h - r) + ((4/3) * pi * (r ** 3)) / 2
		print("Volume:", (round((vol * 1000), 3)), "litros")
	else: 
		vol = pi *(r ** 2) * (H- 2 * r) + (4/3) * pi * (r ** 3)-(pi / 3) *((H- h) ** 2) * (3 * r -(H-h))
		print("Volume:", (round((vol* 1000), 3)), "litros")	
else:
	print("Entradas invalidas")