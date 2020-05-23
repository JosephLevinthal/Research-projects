from numpy import *
from numpy.linalg import *

q = array(eval(input("")))

for i in range(shape(q)[1]):
	
	q[:,i] = sorted(q[:,i] , reverse = True)

print(q)