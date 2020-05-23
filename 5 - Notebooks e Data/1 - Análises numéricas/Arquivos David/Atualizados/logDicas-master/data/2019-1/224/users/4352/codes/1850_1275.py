from numpy import*
from numpy.linalg import*
m = array(eval(input("digite a matriz: ")))
ma = m.shape [0]
z = zeros(ma,dtype=int)
for i in range(ma):
	z[i] = sum(m[i,:])
print(z)
