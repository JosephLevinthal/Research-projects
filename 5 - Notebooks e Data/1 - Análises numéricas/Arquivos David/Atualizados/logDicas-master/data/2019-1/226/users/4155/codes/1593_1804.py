from math import *

cAx = float(input("valor: "))
cAy = float(input("valor: "))
cBx = float(input("valor: "))
cBy = float(input("valor: "))

dAB = float(sqrt((cBx - cAx) ** 2 + (cBy - cAy) ** 2))

r = round(dAB, 3)

print(r)