Xa = float(input("Xa: "))
Ya = float(input("Ya:"))
Xb = float (input("Xb: "))
Yb = float(input("Yb: "))

from math import*
dAB = sqrt((Xb - Xa) ** 2 + (Yb-Ya)) ** 2 
print(round(dAB, 3))