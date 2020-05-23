from numpy import *
from numpy.linalg import *

q = array(eval(input("")))

for i in range(shape(q)[0]):
	
	print(max(q[i,:]))
