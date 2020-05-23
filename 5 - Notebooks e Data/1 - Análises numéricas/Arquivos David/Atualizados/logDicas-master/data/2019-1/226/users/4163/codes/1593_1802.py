from math import*
b = int(input("pontos de vida:"))
d1 = int(input("valor de d1:"))
d2 =int(input("valor de d2:"))

dono = int((sqrt(5*d1))+pi**(d2/3))

print(b-dono)
