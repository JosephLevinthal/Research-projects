from numpy import *
x = array(eval(input()))


a = 0

h = 0
while size(x) > h:
	if x[h] > 99:
		print(h)
		a += 1
	h += 1
print(a)
