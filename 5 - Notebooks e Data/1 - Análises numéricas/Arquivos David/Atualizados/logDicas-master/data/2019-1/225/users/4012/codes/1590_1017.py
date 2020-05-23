from math import *

lat1 = radians(float(input("Digite lat1: ")))
long1 = radians(float(input("Digite long1: ")))
lat2 = radians(float(input("Digite lat2: ")))
long2 = radians(float(input("Digite long2: ")))

R = 6371.01

d = R * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos (long1 - long2))

print("%.2f" % d)

