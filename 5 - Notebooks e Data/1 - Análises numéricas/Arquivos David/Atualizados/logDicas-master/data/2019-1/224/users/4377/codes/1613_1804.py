xa=float(input("xa"))
ya=float(input("ya"))
xb=float(input("xb"))
yb=float(input("yb"))
from math import*
distancia=sqrt((xa-xb)**2+(ya-yb)**2)
print(round(distancia,3))