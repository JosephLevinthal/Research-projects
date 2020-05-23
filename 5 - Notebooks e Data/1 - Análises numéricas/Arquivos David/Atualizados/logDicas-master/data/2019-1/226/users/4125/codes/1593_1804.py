from math import*
xA = float(input("coordenada a: "))
yA = float(input("coordenada a: "))
xB = float(input("coordenada b: "))
yB = float(input("coordenada b: "))

dAB = sqrt(((xB - xA)**2) + ((yB - yA)**2))
print(round(dAB, 3))