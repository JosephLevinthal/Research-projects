from numpy import *
p = array(eval(input('jhjinjknkj')))
e = 0
for i in range(size(p)):
	if p[i]%2==0:
		e = e+1
a = 0
b = 0
c = zeros(e, dtype=int)
for i in range(size(p)):
	if p[i]%2==0:
		c[b] = i
		b = b+1
print(e)
print(c)