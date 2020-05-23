from numpy import*
from numpy.linalg import*
m = array(eval(input("matriz:")))
for i in len(m):
	for j in len(m):
		if(i == j):
			print(round(sum(m[i,j]),2))