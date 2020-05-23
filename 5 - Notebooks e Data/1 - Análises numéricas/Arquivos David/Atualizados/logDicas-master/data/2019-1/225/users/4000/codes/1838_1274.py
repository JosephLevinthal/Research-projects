from numpy import*
from numpy.linalg import*

v = int(input("M:"))
m = zeros((v,v), dtype = int)
v = v-1
k=0
for i in range(v,-1,-1):
	for j in range(v, -1,-1):
		m[i][j] = i+1
		m[j][i] = i+1
print(m)
		
	