from numpy import*

a = float(input())
v0 = float(input())
n = int(input())

t = arange(n)
d = zeros(n)

i = 0

while(i < n):
	d[i] = ((a * (t[i] ** 2)) / 2) + v0 * t[i]
	i = i + 1

print(d)