from numpy import*

v = array(eval(input()))

n = size(v)

s = 0
i = 0
while(i < n):
	s = s + (v[i] ** (1 / 2))
	i = i + 1

m = (s / n) ** 2
print(round(m, 2))