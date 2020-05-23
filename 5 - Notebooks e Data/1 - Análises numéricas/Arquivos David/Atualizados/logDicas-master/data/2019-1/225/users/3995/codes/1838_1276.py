from numpy import*
m=array(eval(input("q:")))
v=zeros(shape(m)[1])
for i in range(shape(m)[1]):
	v[i] = sum(m[:,i])
maximo = max(v)
for i in range(size(v)):
	if(v[i]==maximo):
		print(i+1)
