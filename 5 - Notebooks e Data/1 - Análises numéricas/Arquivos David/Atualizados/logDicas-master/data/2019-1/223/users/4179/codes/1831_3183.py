from numpy import *

v=array(eval(input("Numeros: ")))
v1=zeros(size(v), dtype=int)
j=0
for i in range(size(v)):
	j=j-1
	v1[i]=v[j]
	
print(v1)
	
	