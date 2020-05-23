from numpy import*
from numpy.linalg import*

p=array(eval(input()))
n=shape(p)[0]
m=shape(p)[1]
for i in range(n):
	for j in range(m):
		if(p[i]>p[j]):
			r=min(p[:j])
			print(r)
		elif(p[i]<p[j]):
			e=min(p[i][j])
			print(e)