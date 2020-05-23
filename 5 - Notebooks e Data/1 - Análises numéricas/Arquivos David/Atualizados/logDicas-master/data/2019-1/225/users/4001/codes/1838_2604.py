from numpy import*
from numpy.linalg import*
N = array(eval(input("Horas: ")))
m = shape(N)[0] #No. de linhas

for i in range(m):
	print(max(N[i,:]))