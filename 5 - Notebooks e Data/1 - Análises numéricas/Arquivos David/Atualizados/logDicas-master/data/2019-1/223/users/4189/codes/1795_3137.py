from numpy import *
from math import *
v=array(eval(input("vator:")))
i=0
n=0
while(i<size(v)):
	i=i+1
	n=n+1
	
M=log(exp(v[i])*n)/exp(n)
print(round(M,2))