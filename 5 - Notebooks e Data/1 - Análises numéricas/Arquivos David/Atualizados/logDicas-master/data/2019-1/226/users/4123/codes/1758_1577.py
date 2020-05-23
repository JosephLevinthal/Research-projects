from numpy import*
a = float(input())
v0 = float(input())
n = int(input())
v = arange(n)
v = v*v*a/2 + v0*v
print(v)
