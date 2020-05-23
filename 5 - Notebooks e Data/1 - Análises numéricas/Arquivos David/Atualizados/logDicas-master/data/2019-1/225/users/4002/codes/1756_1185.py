from numpy import *

vet1 = array(eval(input("v: ")))

i = 0 
c1 = 0

while i < len(vet1) :
	if vet1[i] > 99 :
		c1 = c1 + 1
		print(i)
	i+=1
print(c1)