x_a = float(input("abcissa a: "))
y_a = float(input("ordenada a: "))
x_b = float(input("abcissa b: "))
y_b = float(input("ordenada b: "))
from math import *
dist = sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)
print(round(dist,3))