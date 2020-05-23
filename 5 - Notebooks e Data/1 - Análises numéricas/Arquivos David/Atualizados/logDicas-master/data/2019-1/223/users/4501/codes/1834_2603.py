from numpy import*
from numpy.linalg import*
a=array(eval(input("numero: ")))
for i in range(shape(a)[1]):
	a[:,i]=sorted(a[:,i],reverse=True)
print(a)	