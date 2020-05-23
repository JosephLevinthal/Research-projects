from numpy import*

p = array(eval(input()))
f = array(eval(input()))
i = 0
while i<len(p):
	q = p-f
	if q[i]==max(q):
		j = i
	i+=1
print(j+1)