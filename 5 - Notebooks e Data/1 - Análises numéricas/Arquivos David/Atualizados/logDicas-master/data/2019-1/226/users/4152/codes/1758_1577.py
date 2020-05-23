from numpy import *
a = float(input("Aceleracao: "))
v0 = float(input("Velocidade: "))
num = int(input("Numero: "))
t = arange(num)
d = ((a * (t **2)) / 2) + (v0 * t)
print(d)