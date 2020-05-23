from math import *
a = float(input("comprimento 1: "))
b = float(input("comprimento 2: "))
c = float(input("comprimento 3: "))

s= (a + b + c) / 2

area = sqrt(s*(s-a)*(s-b)*(s-c))
print(round(area,5))
