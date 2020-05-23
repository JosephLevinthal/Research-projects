from math import *
d = float(input("tamanho da rosquinha"))
g = float(input("grossura da rosquinha"))
q = float(input("quantidade de rosquinhas"))
massa = (2*pi**2) * (d*g**2)*q
print(round(massa, 2))
