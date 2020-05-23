from numpy import*
from numpy.linalg import*
m = array(eval(input()))
c=0
x = (shape(m)[0]**2-shape(m)[0]) //2
v = zeros((x))
for i in range(shape(m)[0]):
	for j in range(shape(m)[1]):
		if i > j:
			v[c]=m[i][j]
			c = c+1
			
z = min(v)
print(z)
		
	
			
		
			
			
