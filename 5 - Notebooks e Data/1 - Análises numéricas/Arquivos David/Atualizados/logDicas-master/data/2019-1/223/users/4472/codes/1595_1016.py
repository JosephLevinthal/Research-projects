from math import *

lado1 = float(input("Digite o lado 1: "))
lado2 = float(input("Digite o lado 2: "))
lado3 = float(input("Digite o lado 2: "))

s = (lado1 + lado2 + lado3) / 2

A = sqrt( (s * (s - lado1) * (s - lado2) * (s - lado3)))

print(round(A,5))