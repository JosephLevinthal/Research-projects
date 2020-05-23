from math import *
p1_la= radians(float(input("Latitude de P1: ")))
p1_lo= radians(float(input("Longitude de p1: ")))
p2_la= radians(float(input("Latitude de P2: ")))
p2_lo= radians(float(input("Longitude de P2: ")))

d=6371.01*(acos(sin(p1_la)*(sin(p2_la))+(cos(p1_la)*cos(p2_la)*cos(p1_lo-p2_lo))))

print(round(d,2))

