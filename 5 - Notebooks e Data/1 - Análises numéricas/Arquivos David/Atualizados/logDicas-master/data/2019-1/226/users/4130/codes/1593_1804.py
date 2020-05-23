from math import *

xA = float(input("Coordenada xA: "))
yA = float(input("Coordenada yA: "))
xB = float(input("Coordenada xB: "))
yB = float(input("Coordenada yB: "))

x = sqrt((xB - xA)**2 + (yB - yA)**2)

print(round(x, 3))