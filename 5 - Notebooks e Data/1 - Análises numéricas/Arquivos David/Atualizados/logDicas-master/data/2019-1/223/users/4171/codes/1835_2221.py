from numpy import *
from numpy.linalg import *

q = array(eval(input("")))

f = 0

for i in range(shape(q)[0]):
	
	f += (min(q[i,:]))
	h = f / (shape(q)[0])
	h = round(h,2)

print(h)