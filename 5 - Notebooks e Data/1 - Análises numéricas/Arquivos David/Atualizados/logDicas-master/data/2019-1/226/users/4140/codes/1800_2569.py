from numpy import *
v1=array(eval(input()))
m=sum(v1)/size(v1)
soma=0
for i in range(size(v1)):
	soma=soma+(v1[i]-m)**2
d=(soma/(size(v1)-1))**0.5
print(round(d,3))
	