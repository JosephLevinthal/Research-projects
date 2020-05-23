from numpy import*
from numpy.linalg import*
N = array(eval(input("Horas: ")))
m = shape(N)[0] #No. de linhas
z = zeros(m, dtype=int)
c = 0 #contador
for i in range(m):
	z[c] = sum(N[i,:])
	c = c + 1
print(z)
		