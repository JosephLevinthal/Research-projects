from numpy import *
mat = array(eval(input("digite: ")))
for i in range(shape(mat)[0]):
	for j in range(shape(mat)[1]):
		if(i==j):
			prn(mat[i,j])
print(k)