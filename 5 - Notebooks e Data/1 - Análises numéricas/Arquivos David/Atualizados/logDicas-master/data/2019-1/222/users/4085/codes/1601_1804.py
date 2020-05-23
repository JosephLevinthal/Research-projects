XA = float(input("abscissa do pomnto A: "))
YA = float(input("ordenada do ponto A: "))
XB = float(input("abscissa do ponto B: "))
YB = float(input("ordenada do ponto B: "))
from math import *
d = sqrt((XB - XA)**2 + (YB - YA)**2)
print(round(d, 3))