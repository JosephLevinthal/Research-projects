from numpy import *
a = array(eval(input("tempo: ")))
b=zeros(size(a), dtype=int)
c=0
for i in a:
	if ( i != 1):
		c = c + 1
d = zeros(c, dtype = int)
e =0
for i in a:
	if (i!= 1):
		b[e] = a[i]
		e = e + 1
	else:
		b[c] = 1
		c = c + 1


	