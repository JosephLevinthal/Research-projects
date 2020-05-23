from numpy.linalg import *
from numpy import *

m = array(eval(input("Digite: ")))

v = zeros(shape(m)[0]**2-shape(m)[0],dtype=float)
aux=0
for i in range(shape(m)[0]):
	for j in range(shape(m)[1]):
		if(i!=j):
			aux+=m[i,j]
			
aux = aux/size(v)
print(round(aux,2))
