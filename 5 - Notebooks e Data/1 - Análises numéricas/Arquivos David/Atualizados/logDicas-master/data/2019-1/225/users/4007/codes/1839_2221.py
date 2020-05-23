from numpy import*
from numpy.linalg import*
m = array(eval(input("")))
h = 0
c = 0

for i in range(shape(m)[0]):
	h+= (min(m[i,:]))
	c+=1
print(round((h/c),2))
