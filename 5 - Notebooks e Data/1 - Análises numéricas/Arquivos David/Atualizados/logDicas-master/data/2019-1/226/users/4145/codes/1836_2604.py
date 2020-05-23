from numpy import*
from numpy.linalg import*
m =array(eval(input("matriz: ")))

for i in range(shape(m)[0]):
	print(max(m[i]))
