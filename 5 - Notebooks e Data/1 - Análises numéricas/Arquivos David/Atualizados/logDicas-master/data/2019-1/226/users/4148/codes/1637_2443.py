from math import*
r = float(input("raio: "))
x = float(input("altura: "))
n = int(input("numero da opcao: "))

if n==1:
	print(round(pi*x**2*(3*r-x)/3, 4))
	
else:
	print(round(4*pi*r**3 / 3 - pi*x**2*(3*r-x) / 3, 4))
