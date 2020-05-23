from numpy import*
from numpy.linalg import*
matriz = array(eval(input("dig a matriz: ")))
c = matriz.shape [1]
z=zeros((4,4), dtype=int)
for i in range (c):
	for j in range (c):
		matriz[:,j]= sorted(matriz[:,j], reverse = True )
print(matriz)