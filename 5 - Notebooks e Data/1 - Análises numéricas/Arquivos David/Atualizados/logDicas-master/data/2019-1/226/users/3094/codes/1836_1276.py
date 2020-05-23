from numpy import *
from numpy.linalg import *

mit = array(eval(input("jhk:")))
ver = zeros(shape(mit)[1],dtype=int)
for j in range(7):
	for i in range(shape(mit)[0]):
		ver[j]+=mit[i,j]
		
for i in range(size(ver)):
	if(ver[i]==max[i,j]):
		print(i+1)
		