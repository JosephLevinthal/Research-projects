from math import*

xa = float(input("valor de xa: "))
ya = float(input("valor de ya: "))
xb = float(input("calor de xb: "))
yb = float(input("valor de yb: "))

d = ((xb - xa)**2 + (yb - ya)**2)**0.5
print(round(d,3))
