from numpy import *
v = array(eval(input("v: ")))
i = 0
n = 0
while(i < size(v)):
	if(v[i] < 0):
		n = n + 1 
	i = i + 1

tamfinal = size(v) - n
vetfinal = zeros(tamfinal, dtype=int)

i = 0
j = 0
while(i <size(v)):
	if (v[i] >= 0):
		vetfinal[j] = v[i]
		j = j + 1
	i = i + 1
print(vetfinal)