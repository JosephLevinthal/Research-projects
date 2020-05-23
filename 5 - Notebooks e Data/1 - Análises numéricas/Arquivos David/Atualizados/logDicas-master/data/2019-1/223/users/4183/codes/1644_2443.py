from math import *
r = float(input("Digite raio: "))
x = float(input("Digite altura: "))
w = input("Opcao desejada (1/2): ")
va = pi*x**2*(3*r - x)/3
vc = (4*pi*r**3)/3
dva = vc - va
if (w=="1"):
	print(round(va,4))
else: 
	print(round(dva,4))

