from numpy import *

x = array(eval(input()))
h = 0

while size(x) > 1:
	h = 0
	for i in x:
		if 5 <= i < 7:
			h += 1
	print(h)
	x = array(eval(input()))