from numpy import *
from numpy.linalg import *
trafego = array([[1,-1,0,0],
					 [0,1,-1,0],
					 [0,0,1,0],
					 [1,0,0,1]])
inter = array([50,-120,350,870])
resultado = dot(inv(trafego),inter.T)
print(resultado)