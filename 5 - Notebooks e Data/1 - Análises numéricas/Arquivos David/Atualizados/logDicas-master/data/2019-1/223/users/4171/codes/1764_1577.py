from numpy import *

a = float(input("a: "))
v0 = float(input("velocidade inicial: "))
N = int(input("N: "))

t = arange(N)

g = ((a * t**2)/2) + v0 * t

print(g)
