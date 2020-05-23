from numpy import*
from numpy.linalg import*

m = array(eval(input("matriz: ")))

nl = shape(m)[0]
nc = shape(m)[1]
v = zeros(7)
for i in range(nc):
	for j in range(7):
		if i < nl:
			v[j] = m[i,j]
	if max(v)!=0:
		print(max(v))
	v = zeros(7)