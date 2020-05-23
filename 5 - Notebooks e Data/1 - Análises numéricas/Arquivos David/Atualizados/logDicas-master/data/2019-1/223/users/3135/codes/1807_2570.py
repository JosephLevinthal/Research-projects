from numpy import*
from math import*
v= array(eval(input("Insira o bla bla bla:")))
d1=1
me=sum(v)/len(v)

for i in range(size(v)):	
	p=abs(v[i]-me)
	d1=d1*p
s= (d1)**(1/size(v))
print(round(s,3))