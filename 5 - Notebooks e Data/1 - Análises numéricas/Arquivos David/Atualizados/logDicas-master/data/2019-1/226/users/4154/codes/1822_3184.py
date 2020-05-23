from numpy import *
a = array(eval(input()))

d = ''
c = size(a)
b = 0
for j in a:
	for i in a:
		if j > i:
			d = i
			i = j
			j = d
	print(a)