from numpy import *
M =  array(eval(input("")))
v = zeros((len(M)),dtype = int)
for i in range(len(M)):
	v[i] = M[i].sum()
print(v)