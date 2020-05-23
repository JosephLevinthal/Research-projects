from numpy import *
x = array(eval(input()))
y = array(eval(input()))

b = zeros(3, dtype=int)



for i in range(size(x)):
	if x[i] > y[i]:
		b[0] += 1
	if x[i] == y[i]:
		b[1] += 1
	if x[i] < y[i]:
		b[2] += 1
print(b)