from numpy.linalg import*
from numpy import*


vet1=array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])
vet2=array([50,-120,350,870])

c=dot(inv(vet1),vet2)

print(c)
