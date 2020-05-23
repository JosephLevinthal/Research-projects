from math import*
r = float(input("raio: "))
a = float(input("altura "))
b = int(input('nmr da opcao: '))

if b == 1:
	print(round(4*pi*r**3/3-(4*pi*r**3/3-pi*a**2*(3*r-a)/3),4))
else:
	print(round(4*pi*r**3/3-pi*a**2*(3*r-a)/3,4))