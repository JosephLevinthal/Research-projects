from numpy import *

a = float(input())
v = float(input())
n = int(input())

i = 0
h = 0

x = arange(n)
d = zeros(n)

while size(x) > h:
	d[h] = ((a*(x[i]**2))/2) +v*x[i]
	h += 1
	i += 1
print(d)