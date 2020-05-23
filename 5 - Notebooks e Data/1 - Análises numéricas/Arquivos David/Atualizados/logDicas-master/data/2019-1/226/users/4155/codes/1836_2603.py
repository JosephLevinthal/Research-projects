from numpy import*
from numpy.linalg import*
 
x = array(eval(input("v: ")))

x = x

for i in range(4):
	x[:,i] = sorted(x[:,i], reverse = True)
print(x)