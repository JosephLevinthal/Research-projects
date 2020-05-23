from numpy import *

x = array(eval(input()))

h = 0
b = 0
for i in range(size(x)):
	if x[i]%2 == 1:
		h +=1

a = zeros(h,dtype=int)

for i in range(size(x)):
	if x[i]%2 == 1:
		a[b] = x[i]
		b += 1
print(a)