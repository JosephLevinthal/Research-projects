from numpy import *
from numpy.linalg import *

x=array([[1,-1,0,0],
			[0,1,-1,0],
			[0,0,1,0],
			[1,0,0,1]])
y=array([50,-120,350,870])

z=dot(inv(x),y.T)
print(z)