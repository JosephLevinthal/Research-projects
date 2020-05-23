from numpy import*
from numpy.linalg import*

saida = array([50,-120,350,870]).T

equa = array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])

res = dot(inv(equa),saida)

print(res)