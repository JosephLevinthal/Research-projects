from math import *

b = float(input("lado b: "))
c = float(input("lado c: "))
Oa = radians(float(input("angulo bc: ")))


ang = cos(Oa)
lei = 2 * b * c * ang
k = (b ** 2) + (c ** 2) - lei
a = sqrt(k)

print(round(a, 2))