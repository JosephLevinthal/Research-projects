from math import *
a = float(input())
b = int(input())
d = 0
for i in range(b):
	if i%2 != 0:
		d -= a**(i*2)
	else:
		d += a**(i*2)
print(round(d,8))