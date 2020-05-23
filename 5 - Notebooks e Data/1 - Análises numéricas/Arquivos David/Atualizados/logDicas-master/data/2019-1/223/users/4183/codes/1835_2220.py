from numpy import *
from numpy.linalg import *
m = array(eval(input("Digite: ")))
for i in range(m.shape[0]):
	for j in range(7):
		if (m[i,j] == max(m[i])):
			print(m[i,j])

	


		
		