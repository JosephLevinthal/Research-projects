from math import * 
H = float(input(""))
h = float(input(""))
r = float(input(""))
print("Entradas: ", H,",",h,",", r)
if (h < 0 or H < 0 or r <0):
	vol = -1
elif (h <r ):
	vol = (1/3) * pi * h**2 (3 * r - h)
elif (h < H - r):
	vol = (2/3) * pi * r**3 + pi * r**2 * (h - r)
elif (h <= H):
	vol = (4/3) * pi * r**3 + pi * r**2 * (H - 2 * r) - (1/3) * pi * (H - h)**2 * (3 * r - H + h)
else:
	vol = -1
	
print("Volume: ", round(vol, 3),"litros")