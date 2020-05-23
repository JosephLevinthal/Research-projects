from numpy import*
from numpy.linalg import*
mt=array([[1,-1,0,0], [0,1,-1,0], [0,0,1,0], [1,0,0,1]])
r=array([50,-120,350,870])
r=r.T
s=dot(inv(mt),r)
print(s)