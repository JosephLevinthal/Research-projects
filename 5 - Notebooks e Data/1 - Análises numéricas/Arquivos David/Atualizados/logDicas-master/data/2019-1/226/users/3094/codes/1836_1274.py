from numpy import * 
from numpy.linalg import *

z = int(input(""))
met = zeros((z,z), dtype=int)


#met = zeros((z,z), dtype=int)


met = ones((z,z), dtype = int)
nil = zeros((z,z), dtype=int)

for i in range(z):
	for j in range(z):
		nil[i,j]=min(i,j)+1
		
print(nil)