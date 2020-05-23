from numpy import * 
v = array(eval(input('Digite: ')))
m = sum(v) / size(v)
d = 0
for i in range(size(v)):
	d = d + (v[i] - m)**2
d = sqrt(d / (size(v) -1))
print(round(d,3))


	