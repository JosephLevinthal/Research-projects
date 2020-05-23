from numpy import *
x = array(eval(input()))
a = zeros(size(x))
h = 0
e = 0
while size(x) > h:
	if x[h] >= 0:
		a[h] = x[h]
		e += 1
	h += 1
i = 0
f = 0
b = zeros(e,dtype=int)
while  (size(x) > i):
	if( a[i] > 0.0) :
		b[f] = a[i]
		f += 1
	i += 1
print(b)