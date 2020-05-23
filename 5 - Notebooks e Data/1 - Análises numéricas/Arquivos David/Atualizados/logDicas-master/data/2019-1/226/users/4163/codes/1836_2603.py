from numpy import*
from numpy.linalg import*
m = zeros((4,4), dtype=int)
mat = array(eval(input("digite: ")))
for j in range(4):
	for i in range(4):
		x = mat[:,j]
		x = sorted(x, reverse=True)
		m[j:i+1]= x
print(m.T)