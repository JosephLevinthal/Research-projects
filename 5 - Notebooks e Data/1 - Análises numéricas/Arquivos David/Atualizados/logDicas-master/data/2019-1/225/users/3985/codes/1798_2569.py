from numpy import*

v = array(eval(input()))

d1 = 0
m = sum(v)/size(v)

for i in range(size(v)):
	d1 = d1 + (v[i] - m)**2
d2 = sqrt(d1/(size(v) - 1))
print(round(d2, 3))