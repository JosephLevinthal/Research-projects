from numpy import *
a = array(eval(input("digite um vetor a: ")))
b = array(eval(input("digite um vetor b: ")))
inv = zeros(size(b), dtype=int)
i = -1
j = 0
while(i >= -size(a)):
	inv[j] = b[i]
	i = i -1
	j = j+1
x = 0
while(x < size(inv)):
	if(a[x] > inv[x]):
		print(a[x])
	else:
		print(inv[x])
	x = x+1	
