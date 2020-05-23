from numpy import *
from math 
x= array(eval(input("digite: ")))
s=sum(x)
d=0
m=s/size(x)
for i in x:
	d=(i-m)**2+d
g=sqrt(d/(size(x)-1))
print(round(g, 3))