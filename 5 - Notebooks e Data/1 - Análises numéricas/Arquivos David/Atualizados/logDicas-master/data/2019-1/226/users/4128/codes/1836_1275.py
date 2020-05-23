from numpy import*
from numpy.linalg import* 

f = array(eval(input("funcionarios:")))
t = shape(f)[0]
mt = zeros(t,dtype=int)
for i in range(t):
	mt[i] = sum(f[i,:])	

print(mt)
