
from math import*
t1 = radians(float(input("Latitude de P1: ")))
g1=radians(float(input("g1")))
t2=radians(float(input("t2")))
g2=radians(float(input("g2")))
r=6371.01
distancia=r*acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
print(round(distancia,2))