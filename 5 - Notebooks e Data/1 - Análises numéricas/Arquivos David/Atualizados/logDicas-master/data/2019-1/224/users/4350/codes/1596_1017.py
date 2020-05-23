import math
t1 = math.radians(float(input("Latitude de P1: ")))
g1 = math.radians(float(input("Longitude de g1: ")))
t2 = math.radians(float(input("Latitude de P2: ")))
g2 = math.radians(float(input("Longitude de g2: ")))
R = 6371.01
a = R * math.acos(math.sin(t1) * math.sin(t2) + math.cos (t1) * math.cos(t2)*math.cos(g1-g2))
print(round(a, 2))