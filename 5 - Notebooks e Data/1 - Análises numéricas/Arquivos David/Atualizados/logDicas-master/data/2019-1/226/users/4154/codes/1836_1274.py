from numpy import *
from numpy.linalg import *
a = int(input())
b = zeros((a,a),dtype=int)
for i in range(a):
	for j in range(a):
		if i == j:
			b[i,j] = i+1
		elif i > j:
			b[i,j] = j+1
		elif i < j:
			b[i,j] = i+1
			
print(b)