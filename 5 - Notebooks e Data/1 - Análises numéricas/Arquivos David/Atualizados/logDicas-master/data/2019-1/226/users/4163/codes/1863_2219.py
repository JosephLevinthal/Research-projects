from numpy import*
from numpy.linalg import*

mat= array(eval(input("digite: ")))
a = 0
for i in range(shape(mat)[0]):
	for j in range(shape(mat)[1]):
		if i>j:
			a = round(a +  mat[i,j],2)	
m = (mat**2-)			
b = round(a/shape(mat)[0],2)
print(round(b, 2))

			
		
		
		
		