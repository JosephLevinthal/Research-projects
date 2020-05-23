from math import *
n = int(input("pessoas: "))

den1 = factorial(365)
div1 = factorial(365 - n)
par1 = den1 / div1

div2 = 365 ** n
par2 = 1 / div2

p = 1 - (par1 * par2)
pct = p * 100

print(round(pct, 2))