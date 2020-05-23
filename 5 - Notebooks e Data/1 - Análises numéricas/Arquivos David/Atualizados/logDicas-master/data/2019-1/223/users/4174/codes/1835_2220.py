from numpy import*
from numpy.linalg import*

pag = array(eval(input("pagamentos:")))

for i in range(shape(pag)[0]):
	print (max(pag[i,:]))
