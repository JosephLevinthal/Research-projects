from numpy import *
from numpy.linalg import *

x = array(eval(input("Hora do riso: ")))

w = shape(x)[0]

k = zeros(w, dtype=int)

for i in range(w):
	k[i] = sum(x[i,:])
print(k)	