from numpy import*
from math import*
v=array(eval(input("Digite o vetor: ")))
b=sum(v)/size(v)
i=0
for y in v:
	i=i+(y-b)**2
i=sqrt(i/(size(v)-1))
print(round(i,3))
	