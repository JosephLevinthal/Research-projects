from numpy import*
from math import*

x=input("")

a=""
o=0
for i in range(len(x)):
	if x[i]=="a" or x[i]=="A":
		o+=1
	else:
		a+=x[i]
		
print(a)