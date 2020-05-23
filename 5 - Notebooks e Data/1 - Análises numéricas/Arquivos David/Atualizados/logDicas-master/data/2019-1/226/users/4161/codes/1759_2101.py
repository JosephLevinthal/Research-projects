from numpy import*
n = int(input("serie: "))
v = zeros(n, dtype=int)
v[0] = 0
v[1] = 1
t = 2
while t<n:
	v[t] = v[t-1] + v[t-2]
	t = t + 1
print(v)