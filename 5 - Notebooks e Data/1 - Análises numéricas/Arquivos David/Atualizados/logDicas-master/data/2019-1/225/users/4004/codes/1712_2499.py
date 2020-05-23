from math import *
x = int(input("valor de x: "))

s = 0
v = 0

while (v<x):
	s =(s + 1 / factorial(v))
	v = v + 1
print(round((s), 8))
