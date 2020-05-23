from numpy import*
from numpy.linalg import*
m = array(eval(input("m:")))
n= (shape(m)[0])
v = zeros((n**2-n),dtype=float)
c=0
for i in range(shape(m)[0]):
	for j in range(shape(m)[1]):
		n = (shape(m)[0])
		if(i + j != n -1):
			v[c]= m[i][j]
			c=c+1
			t = min(v)
print(t)
		
		
