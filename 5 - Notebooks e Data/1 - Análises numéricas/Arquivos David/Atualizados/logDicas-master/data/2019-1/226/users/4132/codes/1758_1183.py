from numpy import *

v = array(eval(input("Digite: ")))

i = 0 
j = 0
k = 0
cont = 0

while(i<size(v)):
	if(v[i]>0):
		cont = cont+1
	i=i+1
		
v2=arange(cont)

while(k<size(v)):
	if(v[k]>0):
		v2[j]=v[k]
		j=j+1
	k=k+1
	
print(v2)