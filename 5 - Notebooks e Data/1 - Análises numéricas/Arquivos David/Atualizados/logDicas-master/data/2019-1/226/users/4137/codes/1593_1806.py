from math import *
np = int(input("Numero de pessoas:"))
pn = (factorial(365)/(factorial(365 - np)))
pn1 = pn*(1/(365**np))
pn2 = 1-pn1
pn3 = pn2*100
print(round(pn3, 2))