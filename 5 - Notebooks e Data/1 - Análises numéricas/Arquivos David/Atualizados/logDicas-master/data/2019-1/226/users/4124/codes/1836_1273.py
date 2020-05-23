from numpy import *
from numpy.linalg import *
x = array([[1,-1,0,0],
			  [0,1,-1,0],
			  [0, 0,1,0],
			  [1,0,0, 1]])
v = array([50,-120,350,870])
y = dot(inv(x), v.T)
print(y)