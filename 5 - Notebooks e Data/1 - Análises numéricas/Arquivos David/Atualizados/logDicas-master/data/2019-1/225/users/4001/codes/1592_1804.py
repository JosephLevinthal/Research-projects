from math import*
xA = float(input("coordenada:"))
yA = float(input("coordenada:"))
xB = float(input("coordenada:"))
yB = float(input("coordenada:"))

dAB = sqrt((xB - xA)**2 + (yB - yA)**2)
print(round(dAB, 3))