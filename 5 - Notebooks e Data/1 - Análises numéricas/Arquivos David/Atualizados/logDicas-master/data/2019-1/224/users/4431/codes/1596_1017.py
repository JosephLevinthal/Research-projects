from math import *

t1 = radians(float(input("Latitude de P1: ")))
g1 = radians(float(input("Longitude de P1: ")))
t2 = radians(float(input("latitude de P2: ")))
g2 = radians(float(input("Longitude de P2: ")))

d= 6371.01*acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))

print(round(d,2))





