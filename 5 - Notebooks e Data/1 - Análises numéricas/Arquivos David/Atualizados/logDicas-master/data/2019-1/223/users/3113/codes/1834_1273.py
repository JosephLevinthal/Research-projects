from numpy.linalg import*
from numpy import*

v=array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])

d=array([50,-120,350,870])
d=d.T

elementos=solve(v,d)

	
print(elementos)