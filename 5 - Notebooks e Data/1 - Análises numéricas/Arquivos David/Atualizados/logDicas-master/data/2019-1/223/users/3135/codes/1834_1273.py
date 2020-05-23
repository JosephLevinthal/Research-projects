from numpy import*
from numpy.linalg import*

m= array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])

v=array([50,-120,350,870])
v1=v.T
r=solve(m,v1)
print(r)