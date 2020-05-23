from math import*

k = float(input())

e = 0
c = 0

while (c < k):
	e = e + (1/factorial(c))
	c = c + 1
print(round(e,8))	