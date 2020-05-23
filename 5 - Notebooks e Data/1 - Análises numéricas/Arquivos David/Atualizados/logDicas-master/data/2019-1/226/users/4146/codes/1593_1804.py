from math import*

xa = float(input("Xa: "))
ya = float(input("Ya: "))
xb = float(input("Xb: "))
yb = float(input("Yb: "))

d = ((xb - xa)**2 + (yb - ya)**2)**0.5
print(round(d, 3))

