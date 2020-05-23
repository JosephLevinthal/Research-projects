xA = float(input("Cordenada 1: "))
yA = float(input("Coodenada 2: "))

xB = float(input("Coodenada 1: "))
yB = float(input("Coodenada 2: "))

from math import*
dAB = sqrt(((xB-xA)**2)+((yB-yA)**2))
print(round(dAB,3))