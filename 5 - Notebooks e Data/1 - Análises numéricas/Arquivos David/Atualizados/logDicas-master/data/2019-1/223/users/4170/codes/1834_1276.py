from numpy import*
from numpy.random import*
m = array(eval(input("Matriz: ")))
v = zeros(7, dtype=int)
for i in range(7):
	v[i] = sum(m[:,i])
for i in range(7):
	if v[i] == max(v):
		print(i+1)
