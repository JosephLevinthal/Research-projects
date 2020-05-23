from numpy.linalg import*
from numpy import*

m=array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])
n=array([50,-120,350,870])
x=dot(inv(m),n.T)
print(x)