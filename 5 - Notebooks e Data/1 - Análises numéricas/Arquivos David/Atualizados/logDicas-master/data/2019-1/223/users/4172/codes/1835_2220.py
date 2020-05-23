from numpy import*
from numpy.linalg import*

x=array(eval(input("")))

for i in range(x.shape[0]):
	print(max(x[i,:]))
