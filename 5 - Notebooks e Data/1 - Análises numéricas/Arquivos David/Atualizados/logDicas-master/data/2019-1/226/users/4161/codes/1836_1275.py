from numpy import*
from numpy.linalg import*

n = array(eval(input("horario de funcionarios: ")))

x = shape(n)[0]
total = zeros(x,dtype=int)
for i in range(x):
	total[i] = sum(n[i,:])
print(total)