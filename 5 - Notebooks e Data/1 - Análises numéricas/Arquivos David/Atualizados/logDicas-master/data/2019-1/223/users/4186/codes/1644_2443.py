from math import *
a= float(input(" digite raio: "))
b= float(input("digite altura: "))
c= input("opcao desejada (1/2):")
var= pi*b**2*(3*a - b)/3
vc= (4*pi*a**3)/3
d= vc - var

if (c == "1"):
	print(round(var,4))
else: 
	print(round(d, 4))

