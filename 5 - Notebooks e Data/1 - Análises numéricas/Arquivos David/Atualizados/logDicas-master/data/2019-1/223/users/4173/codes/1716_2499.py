from math import*
x = int(input())
n = 0
e = 0
while n < x:
	e = e+(1/factorial(n))
	n += 1
print(round(e,8))