from numpy import *

v = array(eval(input("Digite: ")))
j=0
aux =0
for i in range(size(v)):
	if v[i]%2==0:
		aux+=1
v2 = zeros(aux,dtype=int)
for i in range(size(v)):
	if(v[i]%2==0):
		v2[j]=i
		j+=1
print(aux)
print(v2)
	
