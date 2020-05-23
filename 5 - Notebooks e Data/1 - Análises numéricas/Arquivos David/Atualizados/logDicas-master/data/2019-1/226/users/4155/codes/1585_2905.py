from math import *

lado1 = float(input("valor: "))
lado2 = float(input("valor: "))
lado3 = float(input("valor: "))
 
s = (lado1 + lado2 + lado3) / 2

A = sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))

r = round(A, 5)

print(r)