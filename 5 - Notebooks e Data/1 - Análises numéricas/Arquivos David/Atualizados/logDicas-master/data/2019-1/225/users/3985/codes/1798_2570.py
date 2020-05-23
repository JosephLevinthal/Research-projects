from numpy import*

v = array(eval(input()))

m = sum(v)/size(v)
p1 = 0
for i in range(size(v)):
	if (p1 == 0):
		p1 = abs(v[i] - m)
	elif (p1 > 0):
		p1 = p1 * abs(v[i] - m)

p = (p1) ** (1/size(v))
print(round(p, 3))