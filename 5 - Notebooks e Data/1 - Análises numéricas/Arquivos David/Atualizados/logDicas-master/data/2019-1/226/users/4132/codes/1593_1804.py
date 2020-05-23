from math import *

xa = float(input("Digite o valor de xa: "))
ya = float(input("Digite o valor de ya: "))
xb = float(input("Digite o valor de xb: "))
yb = float(input("Digite o valor de yb: "))

d = sqrt(((xa-xb)**2) + ((ya-yb)**2))

print(round(d,3))