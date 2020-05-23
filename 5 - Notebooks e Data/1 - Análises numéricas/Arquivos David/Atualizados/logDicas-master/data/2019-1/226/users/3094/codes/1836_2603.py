from numpy import *
from numpy.linalg import *

ase = array(eval(input("")))
lg = zeros(shape(ase[1],dtype=int))
for i in range(4):
	for j in range(4):
		lg[j]=ase[j,i]
	lg = sorted(lg,reverse=True)
	for k in range(4):
		ase[k,i]=lg[k]
print(ase)