from numpy import *
from numpy.linalg import *

x = array(eval(input()))

i = shape(x)[0]
j = shape(x)[1]

a = x[0,:]
b = x[1,:]
c = x[2,:]

if max(a) > max(b) > max(c) or max(a) > max(c) > max(b):
	print(max(a))
elif max(b) > max(a) > max(c) or max(b) > max(c) > max(a):
	print(max(b))
elif max(c) > max(b) > max(a) or max(c) > max(a) > max(b):
	print(max(c))
elif max(a) == max(b) and max(b) > max(c) or max(a) == max(b) and max(a) > max(c):
	print(max(a))
elif max(a) == max(c) and max(c) > max(b) or max(a) == max(c) and max(a) > max(b):
	print(max(c))
elif max(b) == max(c) and max(b) > max(a) or max(b) == max(c) and max(c) > max(a):
	print(max(b))
elif max(a) == max(b) == max(c):
	print(max(a))