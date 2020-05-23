from numpy import *
from numpy.linalg import *
m = array(eval(input("Insira uma matriz: ")))
v = zeros(7,dtype=int)
for i in range(m.shape[0]):
	for j in range(7):
		v[j] = v[j] + m[i,j]
for k in range(7):
	if (v[k] == max(v)):
		print(k+1)
