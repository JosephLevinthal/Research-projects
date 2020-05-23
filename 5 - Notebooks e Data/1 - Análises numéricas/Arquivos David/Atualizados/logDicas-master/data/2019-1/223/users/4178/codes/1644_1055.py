from math import *

v = float(input("Velocidade inicial: "))
a = float(input("Angulo do vetor: "))
g = float(input("Aceleracao da gravidade: "))
xx= radians(a)
r = (v)**2 * (sin(2*a))/g

print(r)

