from numpy import *
from numpy.linalg import *

a = array(eval(input("Vetor: ")))

for i in range(shape(a)[0]):
	print(max(a[i]))