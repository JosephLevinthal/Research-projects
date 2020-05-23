from numpy import*
from numpy.linalg import*

mat=array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])

vet= array([50,-120,350,870])

flu=dot(inv(mat),vet.T)

print(flu)

