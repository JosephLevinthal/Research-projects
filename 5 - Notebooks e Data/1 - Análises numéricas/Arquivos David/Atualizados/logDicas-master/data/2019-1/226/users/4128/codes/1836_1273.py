from numpy import*
from numpy.linalg import* 

x = array([50 , -120, 350 , 870])
x = x . T

rua = array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])

y = dot(inv(rua),x)

print(y)
