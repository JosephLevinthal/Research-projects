from numpy import *
from numpy.linalg import *

N = array(eval(input('Insira: ')))
v = shape(N)[1]
m = zeros(v, dtype=int)

for j in range(size(m)):
	m[j] = sum(N[:, j])
for j in range(size(m)):
	if m[j]==max(m):
		a = j+1
		print(a)