from numpy import*
from numpy.linalg import*

v = array(eval(input("Digite as horas: ")))

a = shape(v)[0]
b = zeros((a),dtype= int)

for i in range(a):
	b[i] = sum(v[i,:])

print(b)