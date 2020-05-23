from numpy import*
from numpy.linalg import*
a = array(eval(input()))
y = shape(a)[1]
b = zeros(y, dtype=int)
for j in range(size(b)):
	b[j] = sum(a[:,j]) 
for j in range(size(b)):
	if b[j] == max(b):
		j = j + 1
		print(j)