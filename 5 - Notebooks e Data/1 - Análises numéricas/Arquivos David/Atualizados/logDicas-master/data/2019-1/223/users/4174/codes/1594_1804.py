xa = float(input("cord1:"))
xb = float(input("cord2:"))
ya = float(input("cord3:"))
yb = float(input("cord4:"))

from math import*

formula = float(xb-xa)**2 + (yb-ya)**2
distancia = float(sqrt(formula))
r = round(distancia,3)
 
print(r)