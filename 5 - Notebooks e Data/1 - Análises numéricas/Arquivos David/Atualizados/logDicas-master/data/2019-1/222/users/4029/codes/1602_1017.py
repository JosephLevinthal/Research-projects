import math
t1 = math.radians(float(input("Latitude de P1: ")))
g1 = math.radians(float(input("Longitude de P1: ")))
t2 = math.radians(float(input("Latitude de P2: ")))
g2 = math.radians(float(input("Longitude de P2: ")))
a= math.cos(g1 - g2)
b= math.cos(t2)
c= math.cos(t1)
d= math.sin(t2)
e= math.sin(t1)
f= ((e*d) + (c*b*a))
g= 6371.01*math.acos(f)
print(round(g, 2))