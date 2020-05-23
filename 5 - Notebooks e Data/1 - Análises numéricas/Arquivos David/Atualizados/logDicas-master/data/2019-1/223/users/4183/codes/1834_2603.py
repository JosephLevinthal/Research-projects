from numpy import *
mat = array(eval(input("Digite: ")))
v1 = zeros(4,dtype=int)
v2 = zeros(4,dtype=int)
v3 = zeros(4,dtype=int)
v4 = zeros(4,dtype=int)
for i in range(4):
	v1[i] = mat[i,0]
	v2[i] = mat[i,1]
	v3[i] = mat[i,2]
	v4[i] = mat[i,3]
v1 = sorted(v1,reverse=True)
v2 = sorted(v2,reverse=True)
v3 = sorted(v3,reverse=True)
v4 = sorted(v4,reverse=True)
for i in range(4):
	mat[i,0] = v1[i]
	mat[i,1] = v2[i]
	mat[i,2] = v3[i]
	mat[i,3] = v4[i]
print(mat)
		


