from numpy import*
from numpy.linalg import*
a = array(eval(input()))
b = array(eval(input()))
y = zeros(5, dtype=int)
d = 0
for i in range(size(a)):
	if a[i] == "CENOURA":
		y[i] += 2
	elif a[i] == "FERRO":
		y[i] += 4
	elif a[i] == "DWARVEN":
		y[i] += 8
	elif a[i] == "ELVEN":
		y[i] += 11
	elif a[i] == "DAEDRIC":
		y[i] += 14
for i in range(size(b)):
	d += y[i]*b[i]
print(d)