from numpy import *

c = 0
a = array(eval(input()))
for i in a:
	if i < 5:
		c +=1
j = 0
b = zeros(c, dtype=int)
for i in range(size(a)):
	if a[i] < 5:
		b[j] = i
		j += 1
print(c)
print(b)