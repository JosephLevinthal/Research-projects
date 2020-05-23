from math import *
xa = float(input("Insira a coordenada de xa: "))
ya = float(input("Insira a coordenada de ya: "))
xb = float(input("Insira a coordenada de xb: "))
yb = float(input("Insira a coordenada de yb: "))

dist = sqrt((xb-xa)**2 + (yb-ya)**2)
print(round(dist,3))

