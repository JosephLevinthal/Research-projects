from numpy import *

v = array(eval(input()))
i = 0
a = 0
b = 0
while i < (size(v)):
	if (v[i]>80):
		a = a+(v[i]*(15/100))
	else:
		a = a+v[i]
	i = i+1
b = b+a
print(round(b, 2))