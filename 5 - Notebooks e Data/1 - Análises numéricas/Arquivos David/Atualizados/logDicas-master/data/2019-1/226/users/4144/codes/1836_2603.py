from numpy import *
from numpy.linalg import*
a= array(eval(input("digite: ")))
a =a
for i in range(4):
	a[:,i]=sorted(a[:,i],reverse=True)
print(a)