from numpy import*
from numpy.linalg import*
a = array(eval(input()))
y = zeros(4,dtype=int)
for i in range(size(a)):
	if a[i] == 1:
		y[0] += 1
	elif a[i] == 2:
		y[1] += 1
	elif a[i] == 3:
		y[2] += 1
	elif a[i] == 4:
		 y[3] += 1
print(y)