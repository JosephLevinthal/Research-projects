from math import *
x = int(input())
n = 0
e = 1
h = 0
s = 1
while x > n:
	h += s*(1/(e*(3**n)))
	n += 1
	e += 2
	s = s*-1
h = h*(sqrt(12))
print(round(h,8))