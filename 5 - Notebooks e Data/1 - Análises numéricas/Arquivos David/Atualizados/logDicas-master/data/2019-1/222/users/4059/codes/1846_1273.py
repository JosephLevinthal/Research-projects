from numpy import *
from numpy.linalg import *

m=array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0], [1,0,0,1]])
b=array([50,-120,350,870])
b=b.T
x=dot(inv(m),b)
print(matrix.round(x,1))

