from numpy import*
from math import*
x=array(eval(input("")))

m=sum(x)/size(x)
p=1

for g in x:
	p*=abs(g-m)
	w=p**(1/size(x))
	
print(round(w,3))