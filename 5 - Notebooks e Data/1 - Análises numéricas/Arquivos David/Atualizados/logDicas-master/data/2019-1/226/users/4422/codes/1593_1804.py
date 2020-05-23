from math import * 
xa = float(input("Coordenada: "))
ya = float(input("Coordenada: "))
xb= float(input("Coordenada: "))
yb = float(input("Coordenada: "))
dab = sqrt((xb - xa)**2 + (yb - ya)**2)
print(round(dab, 3))