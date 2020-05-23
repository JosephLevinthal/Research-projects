from numpy import *
x = array(eval(input()))
y = array(eval(input()))

a = 0
b = 0
c = 0
d = 0
e = 0

i = 0
h = 0

while size(x) != h:
	if x[i] == -1:
		a += 1
	if -1 < x[i] <=10:
		b += x[h]
		c += 1
	if 6 <= x[i] <=10:
		d += 1
	if 0 <= x[i] < 6:
		e += 1
	if x[h] == max(x):
		f = y[h]
	h += 1
	i += 1
	
t = b/c
print(a)
print(d)
print(e)
print(round(t,2))
print(f)