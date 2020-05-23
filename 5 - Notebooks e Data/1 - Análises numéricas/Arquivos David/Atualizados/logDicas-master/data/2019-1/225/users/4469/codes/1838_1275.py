from numpy import*

m = array(eval(input()), dtype = int)

v = zeros(shape(m)[0], dtype = int)
for i in range(shape(m)[0]):
	v[i] = sum(m[i,:])

print(v)