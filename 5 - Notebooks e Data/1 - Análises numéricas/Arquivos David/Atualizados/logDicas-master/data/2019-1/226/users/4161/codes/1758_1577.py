from numpy import*
a = float(input("acaleracao: "))
b = float(input("v0: "))
n = int(input("n: "))
t = 0
v = zeros(n, dtype=float)
while t < n:
	d = (a*(t**2))/2 + b*t
	v[t] = v[t] + d
	t = t + 1
print(v)