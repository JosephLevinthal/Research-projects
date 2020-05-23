from math import*
v = float(input("Pontos de vida: "))
vd1 =  int(input("Dado 1: "))
vd2 = int(input("Dado 2: "))
d = int(sqrt(5 * vd1) + (pi ** (vd2 / 3)))
print(int(v - d))