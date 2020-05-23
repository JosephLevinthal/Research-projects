from math import *
xa = float(input("qual a cordenada no ponto A, xa? "))
ya = float(input("qual a cordenada no ponto A, ya? "))
xb = float(input("qual a cordenada no ponto B, xb? "))
yb = float(input("qual a cordenada no ponto B, yb? "))
x = (xb - xa)**2
y = (yb-ya)**2
dAB = sqrt(x+y)
print(round(dAB, 3))