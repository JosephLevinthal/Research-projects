from math import*
r = 6371.01
t1 = radians(float(input("Latitude de P1: ")))
g1 = radians(float(input("Latitude de P1: ")))
t2 = radians(float(input("Latitude de P1: ")))
g2 = radians(float(input("Latitude de P1: ")))

d = r*acos((sin(t1))*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
print(round(d,2))