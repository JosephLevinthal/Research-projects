from numpy import *
a = float(input("Digite: "))
v0 = float(input("Digite: "))
t = int(input("Digite: "))
i = 0
d = zeros(t)
while (i < t):
	d[i] = (a*(i**2))/2 + (v0*i)
	i += 1
print(d)
