# Coordenadas de A (xa, ya):
xa = float(input(" Digite a coordenada xa: "))
ya = float(input(" Digite a coordenada ya: "))

# Coordenadas de B (xb, yb):
xb = float(input(" Digite a coordenada xb: "))
yb = float(input(" Digite a coordenada yb: "))

# Distancia entre A e B (d):
from math import sqrt
d = sqrt ((xb - xa)** 2 + (yb - ya)** 2)

print(round(d,3))

