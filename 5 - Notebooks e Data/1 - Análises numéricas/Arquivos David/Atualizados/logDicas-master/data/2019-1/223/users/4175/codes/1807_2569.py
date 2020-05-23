from numpy import *

x = array(eval(input()))

d=0

m=sum(x)/size(x)

for i in x:
	d += (i - m)**2
	w = d / (size(x)-1)
	q = sqrt(w)
print(round(q,3))