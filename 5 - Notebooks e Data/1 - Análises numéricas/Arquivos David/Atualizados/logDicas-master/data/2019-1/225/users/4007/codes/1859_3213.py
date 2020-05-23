from numpy import*
from numpy.linalg import*
m = array(eval(input("matricula: ")))
v = array(eval(input("tempo: ")))
for i in m:
	a = array([m[i]],[v[i]])
print(a)

