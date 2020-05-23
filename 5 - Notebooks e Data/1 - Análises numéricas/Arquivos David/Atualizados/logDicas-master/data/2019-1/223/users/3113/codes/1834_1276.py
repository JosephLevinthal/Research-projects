from numpy import*
from numpy.linalg import*
m=array(eval(input("")))
#contar as linhas

#contador
d=zeros(7,dtype=int)
for i in range(7):
	d[i]=sum(m[:,i])

for i in range(7):
	if(d[i]>=max(d)):
		print(i+1)