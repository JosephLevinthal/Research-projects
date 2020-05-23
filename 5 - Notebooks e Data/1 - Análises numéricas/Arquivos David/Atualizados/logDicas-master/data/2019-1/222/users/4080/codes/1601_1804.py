x1 = float(input("Xa: "))
y1 = float(input("Ya: "))
x2 = float(input("Xb: "))
y2 = float(input("Yb: "))
from math import*
dAB = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(round(dAB,3))
