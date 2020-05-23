from numpy import *

var=array(
	eval
	(input
	 ("vetor:")))
x=sum(var)
y=size(var)
z=x/y

print(size(var))
print(var[0])
print(var[4])
print(max(var))
print(min(var))
print(sum(var))
print(round(z, 2))