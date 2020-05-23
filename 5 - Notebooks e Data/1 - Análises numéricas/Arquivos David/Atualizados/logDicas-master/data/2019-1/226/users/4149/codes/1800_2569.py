from numpy import*
from math import*
v=array(eval(input("entre com o vetor:")))

m= sum(v)/size(v)
i=0
for y in v:
	i=i+(y-m)**2
i=sqrt(i/(size(v)-1))
print(round(i,3))

