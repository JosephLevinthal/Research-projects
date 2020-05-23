from numpy import *
from numpy.linalg import *

m = array(eval(input("Matrizes: ")))
m = m

for i in range(4):
	m[:,i] = sorted(m[:,i], reverse = True)
print(m)	