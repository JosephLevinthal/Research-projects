from numpy import *
from numpy.linalg import *

X = array([[1,-1,0,0], 
			 [0,1,-1,0], 
			 [0,0,1,0], 
			 [1,0,0,1]])

V = array([50,-120,350,870])
k = dot(inv(X) , V.T)
print(k)
