from numpy import*
from numpy.linalg import*
mat=array(eval(input("digite: ")))
#lin=shape(mat)[0]
#col=shape(mat)[1]
#v=(zeros(num),dtype=int)
s=0
for i in range (shape(mat)[0]):
	for j in range(shape(mat)[1]):
		if(j>i):
			s=s+mat[i,j]
print(round(s,2))
			
		