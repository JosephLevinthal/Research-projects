from numpy import*
from numpy.linalg import*
m = array(eval(input("matriz: ")))
n = shape(m)[0]
v= zeros(n-1)
vm = zeros(n)
a = n - 1
for i in range(n):
	for j in range(n):
		if j < n - 1:
			if j!=a:
				v[j] = m[i,j]
			else:
				a = a - 1
	vm[i] = max(v)
print(max(vm))
