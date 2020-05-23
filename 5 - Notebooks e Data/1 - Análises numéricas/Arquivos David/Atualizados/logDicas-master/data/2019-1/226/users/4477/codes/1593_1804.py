# Modulo math
from math import *
# Entradas
xa = float(input("Determine: "))
ya = float(input("Determine: "))
xb = float(input("Determine: "))
yb = float(input("Determine: "))
# Variavel
dist = sqrt((xb -xa)**2 + (yb - ya)**2)
# Saida
print(round(dist, 3))