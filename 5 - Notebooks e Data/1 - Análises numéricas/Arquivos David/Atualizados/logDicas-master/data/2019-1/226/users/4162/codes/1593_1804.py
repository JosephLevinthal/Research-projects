corxa=float(input("coordenadas do eixo xa: "))
corya=float(input("coordenadas do eixo ya: "))
corxb=float(input("coordenadas do eixo xb: "))
coryb=float(input("coordenadas do eixo yb: "))
from math import*
dam=sqrt((corxb-corxa)**2+(coryb-corya)**2)
print(round(dam,3))