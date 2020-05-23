xa = float(input("digite Xa: "))
ya = float(input("digite Ya: "))
xb = float(input("digite Xb: "))
yb = float(input("digite Yb: "))

from math import * 
distancia = sqrt((xb - xa)**2 + (yb - ya)**2)

print(round(distancia, 3))