from numpy import*
from numpy.linalg import*

saida = array([50, -120, 350, 870])
saida = saida.T # transformar linha em coluna - opercaoa matricial

eq = array([          #indices - na frente de x1, x2, x3,x4
	[1,-1,0,0],
	[0,1,-1,0],
	[0,0,1,0],
	[1,0,0,1]])
saida = dot(inv(eq),saida)
print(saida)
	

