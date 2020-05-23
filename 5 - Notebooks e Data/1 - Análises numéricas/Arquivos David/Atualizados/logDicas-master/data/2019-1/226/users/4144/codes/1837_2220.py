from numpy import *
mat= array(eval(input("digite: ")))
for i in range(shape(mat)[0]):
	mat[i,:]=max(mat[i,:])
	print(max(mat[i,:]))