import math

t1 =math.radians(float(input("Latitude de P1: ")))
g1=math.radians(float(input("longitude de p1:")))
t2=math.radians(float(input("latitude de p2:")))
g2=math.radians(float(input("longitude de p2:")))

R= 6371.01

d=r*(math.acos(math.sin(t1)*math.sin(t2)+(math.cos(t1)*math.cos(t2)*math.cos(g1-g2))))
print(round())


