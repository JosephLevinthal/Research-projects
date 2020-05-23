#Descubra qual o valor de "a"

b = float(input(" NUMERO "))
c = float(input(" NUMERO "))
alfa = float(input(" ANGULO "))

from math import *

m = radians(alfa)

x = b**2
y = c**2
z = 2*b*c*cos(m)

a = sqrt(x + y - z)

print(round(a, 2))