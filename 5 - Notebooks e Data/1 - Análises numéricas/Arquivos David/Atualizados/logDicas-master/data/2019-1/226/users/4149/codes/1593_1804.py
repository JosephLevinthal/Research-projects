from math import *
x1= float(input("coloque as coordenadas do ponto x1: "))
y1= float(input("coloque as coordenadas do ponto y1: "))
x2=float(input("coloque as coordenadas do ponto x2: "))
y2=float(input("coloque as coordenadas do ponto y2: "))

dab= sqrt((x2-x1)**2+(y2-y1)**2)
print(round(dab,3))