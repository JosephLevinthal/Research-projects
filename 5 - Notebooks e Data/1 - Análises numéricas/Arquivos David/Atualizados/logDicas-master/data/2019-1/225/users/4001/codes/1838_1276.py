from numpy import*
from numpy.linalg import*
N = array(eval(input("Horas: ")))
z = zeros(7, dtype=int)
c = 0 #contador
for j in range(7):
	z[c] = sum(N[:,j])
	c = c + 1
c = 0
for j in range(7):
	if max(z) == sum(N[:,j]):
		print(j + 1)
	c = c + 1	