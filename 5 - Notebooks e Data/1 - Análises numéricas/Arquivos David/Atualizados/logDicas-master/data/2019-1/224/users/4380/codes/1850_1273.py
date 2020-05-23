from numpy import *
from numpy.linalg import *
mat=array ([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])
resp=array([50,-120,350,870])
r=dot(inv(mat),resp.T)
print(r)