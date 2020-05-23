from numpy import* 
from math import*
v= array(eval(input("Insira o bla bla bla:")))
d1=0
me=sum(v)/len(v)

for i in range(size(v)):		
	d=(v[i]-me)**2
	d1=d1+d
s=(d1/(size(v)-1))**0.5
print(round(s,3))