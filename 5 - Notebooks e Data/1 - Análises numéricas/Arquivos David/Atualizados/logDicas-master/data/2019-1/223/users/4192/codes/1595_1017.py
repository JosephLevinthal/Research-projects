# Importarfuncoes do math
from math import *

t1 = radians(float(input("Latitude de P1: ")))
g1 = radians(float(input("Longitude de P1: ")))
t2 = radians(float(input("Latitude de P2: ")))
g2 = radians(float(input("Longitude de P2: ")))

# Raio medio da Terra
R = 6371.01

# Distancia entre dois pontos P1 e P2, em Km
d = R*acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
print(round(d, 2))

