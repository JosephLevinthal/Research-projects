from numpy import*
from numpy.linalg import*

n = array(eval(input("Digite as horas de trabalho: ")))

a = shape(n)[0]
b = zeros(a)
for i in range(a):
	b[i] = max(n[i,:])
	print(b[i])
	