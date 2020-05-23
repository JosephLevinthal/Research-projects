from numpy import*
from numpy.linalg import*
x = array(eval(input("digite x: "))) 
for i in range(4):
	x[:,i] = sorted(x[:,i], reverse=True)
print(x)