from numpy import*
from numpy.linalg import*
matriz=array(eval(input("dig a matriz: ")))
d = matriz.shape [0]
z = zeros(d, dtype = int)
for i in range (d):
	z[i] = sum(matriz[i,:])
print(z)

		