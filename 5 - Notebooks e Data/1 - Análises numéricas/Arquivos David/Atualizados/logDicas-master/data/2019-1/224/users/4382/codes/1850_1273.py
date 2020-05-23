from numpy import *
from numpy.linalg import *
transito = array([[1,-1,0,0], 
						[0,1,-1,0],
						[0,0,1,0],
				 		[1,0,0,1]])
inter = array ([50,-120,350,870])
resultado=dot(inv(transito),inter.T)
print(resultado) 