from numpy import *
a = array(eval(input()))
c = 0
for i in a:
	if i%2 != 0:
		c += 1
b = zeros(c, dtype = int)
d = 0
for i in a:
	if i%2 != 0:
		b[d] = i
		d += 1
print(b)