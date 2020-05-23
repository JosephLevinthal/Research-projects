from math import*
xa = float(input("coordenada x de a: "))
ya = float(input("coordenada y de a: "))
xb = float(input("coordenada x de b: "))
yb = float(input("coordenada y de b: "))

dab = sqrt((xb-xa)**2  + (yb-ya)**2)
print(round(dab,3))