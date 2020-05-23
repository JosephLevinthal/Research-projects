from numpy import *

v=array(eval(input("Digite vetor: ")))*1.0

n = size(v)
soma=0.0
i =0 
while(i<n):
	soma += v[i]**-1
	i+=1
	
media = (soma/n)**-1

print(round(media,2))
