from numpy import *
from numpy.linalg import *
M = array([[1 ,-1 ,0,0], [0 ,1 , -1,0 ], [0 ,0  ,1,0 ],[1,0,0,1]])
a = array([50,-120,350,870])
r = dot(inv(M),a.T)
print(r)