from math import*
x = float(input())
k = int(input())
i = s = 0
while i<k:
	s += (x**i)/factorial(i)
	i += 1
print(round(s,9))