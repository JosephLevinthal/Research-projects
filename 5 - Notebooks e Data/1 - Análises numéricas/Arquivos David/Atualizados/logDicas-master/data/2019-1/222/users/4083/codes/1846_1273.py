from numpy import*
from numpy.linalg import*

m = array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])
a = array([50,-120,350,870])
d = dot(inv(m), a.T)
print(d)
