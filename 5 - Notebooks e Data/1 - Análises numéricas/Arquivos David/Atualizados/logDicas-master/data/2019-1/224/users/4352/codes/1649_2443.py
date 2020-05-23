r = float(input("digite o raio: "))
x = float(input("digite a altura: "))
n = float(input("digite o tipo de volume 1 ou 2: ")) #1 é n1, 2 é n2

from math import *
n11 = (4 * (pi *(r ** 3)))/3 #volume da esfera = combustível 
n1 = ((pi * (x**2)) * ((3 * r) - x))/3 #calota esférica = volume de ar
n2 = n11 - n1

if n == 1:
	print(round(n1, 4))
else:
	print(round(n2, 4))