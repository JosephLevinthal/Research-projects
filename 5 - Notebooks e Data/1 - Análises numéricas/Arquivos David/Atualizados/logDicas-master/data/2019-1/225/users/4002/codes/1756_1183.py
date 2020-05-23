from numpy import *

v = array(eval(input("vet: ")))
i = 0
c = 0 
while(i < len(v)):
	if v[i] > 0 :
		c = c + 1
	i+=1
a = array([0]*c)
i = 0
j = 0
while(i < len(v)):
	if v[i] > 0:
		a[j] = v[i]
		j = j + 1 
	i+=1
print(a)