from math import *
k = int(input("k: "))
t = 1
e = 1
while (k > 0 and k != t):
	e = e + 1/factorial(t)
	t = t + 1
print(round(e, 8))