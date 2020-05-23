from numpy import*
from numpy.linalg import* 
a = array(eval(input("horario: ")))
b = shape(a)[0]
tot = zeros(b,dtype=int)
for i in range(b):
	tot[i]=sum(a[i,:])
	
print(tot)