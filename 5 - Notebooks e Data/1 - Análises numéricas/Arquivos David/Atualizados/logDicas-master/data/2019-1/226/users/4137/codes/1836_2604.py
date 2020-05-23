from numpy import*
from numpy.linalg import*

n = array(eval(input("Pagamentos:")))

for i in range(shape(n)[0]):
	print(max(n[i]))
