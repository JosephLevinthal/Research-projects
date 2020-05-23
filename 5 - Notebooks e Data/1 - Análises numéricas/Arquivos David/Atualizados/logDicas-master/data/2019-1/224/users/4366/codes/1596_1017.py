from math import*
t1=radians(float(input("Latitude de P1:")))
g1=radians(float(input("Longitude de P1:")))
t2=radians(float(input("Latitude de P2:")))
g2=radians(float(input("Longitude de P2:")))
r=6371.01
d=r*(acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2)))
print(round(d,2))