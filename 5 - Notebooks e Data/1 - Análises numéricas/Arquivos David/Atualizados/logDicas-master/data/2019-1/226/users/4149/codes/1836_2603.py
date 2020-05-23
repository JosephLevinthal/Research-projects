from numpy import*
from numpy.linalg import*

b=array(eval(input("a")))
		  
		  
b = b
		  
		  
for i in range(4):
	b[:,i]=sorted(b[:,i], reverse=True)

print(b)