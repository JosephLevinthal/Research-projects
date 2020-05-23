from numpy import*
from numpy.linalg import*

matriz=array(eval(input("Matriz quadrada:")))
matriz=matriz.T
if (shape(matriz)[:])==(shape(matriz)[:j]):
	print("SIMETRICA")
else:
	print("ASSIMETRICA")
	