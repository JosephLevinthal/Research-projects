from numpy import *
x = array(eval(input()))

a = size(x)
b = 0
h = 0
i = 0
e = 1/3

while a > h:
	m = x[i]**e
	b += m
	i += 1
	h += 1
c = (b/a)**3
print(round(c,2))