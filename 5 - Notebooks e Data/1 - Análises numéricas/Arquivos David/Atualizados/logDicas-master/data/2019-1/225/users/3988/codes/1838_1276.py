from numpy import *
M =  array(eval(input("")))
v = zeros((7),dtype = int)
k= 0
for i in range(len(M)):
	for j in range(len(M[0])):
		v[j]+=M[i][j]
maior = v.max()
for i in range(len(v)):
	if(v[i] == maior):
		print(i+1)