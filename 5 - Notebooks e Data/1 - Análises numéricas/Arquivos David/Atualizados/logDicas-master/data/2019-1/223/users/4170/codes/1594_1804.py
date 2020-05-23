from math import*
xa = float(input("Insira a coordenada xa: "))
ya = float(input("Insira a coordenada ya: "))
xb = float(input("Insira a coordenada xb: "))
yb = float(input("Insira a coordenada yb: "))
d = sqrt((xb-xa)**2 + (yb-ya)**2)
print(round(d,3))