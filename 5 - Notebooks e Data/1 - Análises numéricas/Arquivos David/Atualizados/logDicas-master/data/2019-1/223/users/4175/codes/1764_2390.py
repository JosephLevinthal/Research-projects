from numpy import *

x = array(eval(input()))
y = array(eval(input()))

h = 0
a = 1
b = 1

c = arange(size(x),dtype = int)

while size(c) > h:
	c[h] = x[h] - y[h]
	
	if max(c) > c[h]:
		a += 1
	else:
		b += 1
	h += 1

print(b)