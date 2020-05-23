from numpy import*
from numpy.linalg import*

n = array(eval(input("digite n: ")))

n1 = shape(n)[0]
total = zeros(n1, dtype=int)
for i in range(n1):
	total[i] = sum(n[i,:])
print(total)
