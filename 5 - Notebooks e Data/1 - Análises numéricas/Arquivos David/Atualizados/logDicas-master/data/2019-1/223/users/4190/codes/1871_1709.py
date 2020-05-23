from numpy import *
from numpy.linalg import*

m = array(eval(input('m: ')))
n = int(input('n: '))
a = shape(m)[0]

for i in range(size(m)):
		b = mean(m[i,:])
		
print(round(b, 2)