from numpy import*
v = array(eval(input("v:")))
i = 0
p = 1
d = 0
while(i<size(v)):
	d = d + v[i] * 1 * p
	i = i + 1
	p = p + 1
print(d)