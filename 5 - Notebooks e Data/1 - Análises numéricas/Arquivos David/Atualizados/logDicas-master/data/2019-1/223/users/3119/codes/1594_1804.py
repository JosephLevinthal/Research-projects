from math import*

#Coordenadas do ponto A
Xa = float(input("Xa: "))
Ya = float(input("Ya: "))

#Coordenadas do ponto B

Xb = float(input("Xb: "))
Yb = float(input("Yb: "))

D = sqrt((Xb - Xa)**2 + (Yb - Ya)**2)
print(round(D,3))