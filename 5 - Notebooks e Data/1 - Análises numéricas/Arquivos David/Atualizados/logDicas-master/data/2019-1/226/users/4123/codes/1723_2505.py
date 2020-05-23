from math import*
x = eval(input())
k = int(input())
i = 0
s = 0

while i<k:
	s += ((x**(1+2*i))/(factorial(1+2*i)))*(-1)**i
	i += 1
print(round(s,10))