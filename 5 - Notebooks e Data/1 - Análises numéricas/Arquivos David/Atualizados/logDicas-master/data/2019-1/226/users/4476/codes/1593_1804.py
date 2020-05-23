a = float(input("coordenadas xa: "))
b = float(input("coordenadas ya: "))
c = float(input("coordenadas xb: "))
d = float(input("coordenadas yb: "))
from math import *
var1 = (c-a)** 2
var2 = (d-b)** 2
dab = sqrt(var1 + var2)
print(round(dab, 3))