from numpy import*
from numpy.linalg import*

v = array(eval(input("v: ")))

dba = zeros(shape(v)[1], dtype=int)

for i in range(shape(v)[1]):
	dba[i] = sum(v[:,i])

for i in range(size(dba)):
	if dba[i] == max(dba):
		print(i+1)