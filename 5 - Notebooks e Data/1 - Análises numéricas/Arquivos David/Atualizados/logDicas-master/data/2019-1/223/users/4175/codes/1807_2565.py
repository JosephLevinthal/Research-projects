from numpy import *
x = array(eval(input()))
y = array(eval(input()))
z = int(input())

a = zeros(3,dtype=int)

for i in range(size(x)):
	if x[i] >= 5 and y[i] >= (z*0.75):
		a[0] += 1
	if x[i] < 5:
		a[1] += 1
	if x[i] >= 5 and y[i] < (z*0.75):
		a[2] += 1
print(a)

