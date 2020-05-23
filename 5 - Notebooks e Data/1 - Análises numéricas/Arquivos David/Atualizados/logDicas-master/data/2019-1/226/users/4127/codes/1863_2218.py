from numpy import*
from numpy.linalg import*

a= array(eval(input("digite a dimensao da sua matriz")))

t=0
for i in range(shape(a)[0]):
	for j in range(shape(a)[1]):
		if(j>i):
			t=t+a[i,j]
print(round(t,2))
		
			