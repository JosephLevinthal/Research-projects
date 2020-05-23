from numpy import *
from numpy.linalg import *
m = array(eval(input("Digite: ")))
x = 10
for i in range(m.shape[0]):
	for j in range(m.shape[1]):
		if (m[i,j] <= x):
			x = m[i,j]
print(x)