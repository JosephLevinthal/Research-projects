from math import *
r = float(input("raio:"))
ax = float(input("altura de x:"))
x = int(input("opcao 1 ou 2:"))

if (x == 1):
	v = ((pi*(ax**2))*((3*r)-ax)/3)
else:
	v = ((4*pi*(r**3))/3)-((pi*(ax**2))*((3*r)-ax)/3)

print(round(v,4))