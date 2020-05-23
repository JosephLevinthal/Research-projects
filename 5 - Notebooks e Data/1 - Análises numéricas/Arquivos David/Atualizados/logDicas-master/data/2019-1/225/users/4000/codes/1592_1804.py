xa = float(input("coordenadas do ponto a"))
xb = float(input("coordenadas do ponto a"))
ya = float(input("coordenadas do ponto b"))
yb = float(input("coordenadas do ponto b"))
from math import*
dab = sqrt(xb - xa)**2 + (yb - ya)**2
print(round(dab, 3))