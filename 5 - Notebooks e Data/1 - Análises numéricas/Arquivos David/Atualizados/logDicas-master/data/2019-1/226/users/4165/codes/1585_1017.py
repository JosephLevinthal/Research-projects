
from math import *
t1 = radians(float(input("Latitude de P1: ")))
g1 = radians(float(input("longitude de p1: ")))
t2 = radians(float(input("Latitude de P2: ")))
g2 = radians(float(input("longitude de p2: ")))
distancia = 6371.01*acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1 - g2))
print(round(distancia,2))