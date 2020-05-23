from numpy import*
from numpy.linalg import*
m = array(eval(input("digite uma matriz: ")))
n = m.shape [1]
z = zeros((4,4), dtype=int)
for i in range(n):
	for j in range(n):
		m[:,j] = sorted(m[:,j], reverse=True)
print(m)