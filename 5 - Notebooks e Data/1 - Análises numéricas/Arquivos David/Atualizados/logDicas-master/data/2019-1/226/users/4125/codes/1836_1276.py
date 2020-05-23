from numpy import*
from numpy.linalg import*

n = array(eval(input("digite n: ")))

n1 = shape(n)[0]
x = zeros(7, dtype= int)
for i in range(size(x)):
	x[i]= sum(n[:,i])
for j in range(size(x)):
	if(x[j]==max(x)):
		print(j + 1)