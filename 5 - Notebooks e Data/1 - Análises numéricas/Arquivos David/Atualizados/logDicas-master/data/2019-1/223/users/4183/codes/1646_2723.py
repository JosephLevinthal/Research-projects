from math import *
b = float(input("Digite: "))
c = float(input("Digite: "))
angulo = radians(float(input("Digite: ")))
form = ((b**2) + (c**2)) - (2*b*c*cos(angulo))
var = sqrt(form)
print(round(var,2))