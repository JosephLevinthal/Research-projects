from numpy import *

x = array(eval(input()))

h = 0

for i in range(size(x)):
	if x[i] >= 70:
		h += 1
	
a = zeros(h,dtype=int)
b = 0

for i in range(size(x)):
	if x[i] >= 70:
		a[b] = i
		b += 1
		
print(h)
print(a)