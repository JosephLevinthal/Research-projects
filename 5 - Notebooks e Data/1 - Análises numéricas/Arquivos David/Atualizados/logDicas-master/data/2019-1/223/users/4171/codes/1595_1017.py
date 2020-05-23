from math import *

t1 = radians(float(input("Angulo: ")))
g1 = radians(float(input("Angulo: ")))
t2 = radians(float(input("Angulo: ")))
g2 = radians(float(input("Angulo: ")))

R = 6371.01

d = R * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

print(round(d,2))