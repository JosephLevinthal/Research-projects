xa=float(input("cordenada do ponto xA: "))
ya=float(input("cordenada do ponto yA: "))
xb=float(input("cordenada do ponto xB: "))
yb=float(input("cordenada do ponto yB: "))
from math import*
d=sqrt((xb-xa)**2+(yb-ya)**2)
print(round(d,3))