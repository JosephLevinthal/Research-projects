from numpy import *
a=array(eval(input("vetor: ")))
p=0
b=0
while(p<size(a)):
	if (a[p]>0):
		b = b + 1
	p = p + 1
c = 0
d=0
e = zeros(b,dtype=int)
while(c < size(a)):
	if (a[c] > 0):
		e[d] = a[c]
		d = d +1
	c = c + 1
print(e)