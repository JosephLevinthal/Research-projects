from math import*
t1=radians(float(input("latitude de P1: ")))
g1=radians(float(input("longitude de p1:")))
t2=radians(float(input("latitude de p2:")))
g2=radians(float(input("longitude de p2:")))
R=6371.01
d=R*acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
print(round(d,2))

