from numpy import *

a = float(input("A: "))
v = float(input("V: "))
num = int(input("N: "))

t0 = arange(num, dtype=int)
#print(t0)
d0 = zeros(num, dtype=float)
#print(d0)

d = ((a * (t0**2)) / 2) + v*t0

print(d)