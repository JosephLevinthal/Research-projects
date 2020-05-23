from numpy import*
from numpy.linalg import*
m = array(eval(input("digite a matriz: ")))
n = m.shape [1]
z = zeros(n, dtype=int)
for j in range(n):
	z[j] = sum(m[:,j])
for k in range(size(z)):
	if z[k] == max(z):
		print(k+1)