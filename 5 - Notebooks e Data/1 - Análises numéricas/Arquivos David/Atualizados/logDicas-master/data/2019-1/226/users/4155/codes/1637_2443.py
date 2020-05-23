from math import *
r = float(input("raio:"))
x = float(input("altura:"))
o = int(input("opcao desejada:"))

if(o == 1):
	msg = ((pi * x ** 2) * (3 * r - x)) / 3
else:
	msg = ((4 * pi * r ** 3) / 3) -  (((pi * x ** 2) * (3 * r - x)) / 3)
	
t = round(msg, 4)

print(t)