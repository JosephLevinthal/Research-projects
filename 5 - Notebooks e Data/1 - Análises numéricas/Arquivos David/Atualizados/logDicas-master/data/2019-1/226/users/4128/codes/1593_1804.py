from math import*
xa = float(input("linha1: "))
ya = float(input("linha2: "))
xb = float(input("linha3: "))
yb = float(input("linha4: "))

dab = sqrt((xb-xa)**2+(yb-ya)**2)
print(round(dab,3))