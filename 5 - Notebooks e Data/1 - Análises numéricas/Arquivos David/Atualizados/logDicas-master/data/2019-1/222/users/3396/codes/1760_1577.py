from numpy import *

a = float(input())
v = float(input())
n = int(input())

i = 0
t = arange(n)
tam = n
d = zeros(tam, dtype=float)

while n > i:
    d[i] = ((a * (t[i] ** 2)) / 2) + v * t[i]
    i = i +1
print(d)