from numpy import*
from numpy.linalg import*

x=array(eval(input(" ")))



for i in range(x.shape[0]):
	x[:,i]=sorted(x[:,i],reverse=True)
print(x)
	

