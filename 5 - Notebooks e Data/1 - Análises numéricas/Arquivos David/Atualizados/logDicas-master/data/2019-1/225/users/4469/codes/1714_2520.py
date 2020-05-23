from math import*

n = int(input())

s = 0
c = 1

while(c <= n):
	s = s + (1 / (c ** 2))
	c = c + 1

p = sqrt(s * 6)
print(round(p, 6))