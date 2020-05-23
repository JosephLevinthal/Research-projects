from numpy import *
M =  array(eval(input("")))
v = zeros((len(M)),dtype = int)
for i in range(len(M)):
	for j in range(len(M)):
		v[j] = M[j][i]
	v = sorted(v,reverse=True)
	for j in range(len(M)):
		 M[j][i] = v[j]
print(M)