from numpy import *
v = array(eval(input("v: ")), dtype=int)

i = 0
j = 0
k = 0
p = 0

while(i < size(v)):
	if (v[i] > 0):
		p = p + 1
	i = i + 1
		

d = array(zeros (p), dtype=int)

while (j < size(v) and k < size(d)):
	if (v[j] >= 0):
		d[k] = d[k] + v[j]
		j = j + 1
		k = k + 1
	elif(v[j] < 0):
		j = j + 1

		
print(d)
