from math import*
XA = float(input('XA:'))
YA = float(input('YA:'))
XB = float(input('XB:'))
YB = float(input('YB:'))
distancia = sqrt((XB-XA)**2 + (YB-YA)**2)

print(round(distancia, 3))