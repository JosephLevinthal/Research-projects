from numpy import*
from numpy.random import*
m = array(eval(input("Matriz: ")))
v = zeros(m.shape[0], dtype=int)
for i in range(m.shape[0]):
	v[i] = sum(m[i,:])
print(v)	