from math import*
x1 = float(input("Digite a coordenada x1: "))
y1 = float(input("Digite a coordenada y1: "))
x2 = float(input("Digite a coordenada x2: "))
y2 = float(input("Digite a coordenada y2: "))

dist = sqrt((x2-x1)**2 + (y2-y1)**2)
print(round(dist, 3))