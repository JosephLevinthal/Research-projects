from math import*

a = float(input("digite Xa: "))
b = float(input("digite Ya: "))
c = float(input("digite Xb: "))
d = float(input("digite Yb: "))

dAB = sqrt((((c-a)**2)) + ((d-b)**2))

print(round(dAB, 3))