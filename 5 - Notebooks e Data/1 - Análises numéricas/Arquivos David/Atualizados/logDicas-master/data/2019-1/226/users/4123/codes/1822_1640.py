from numpy import*
q = array(eval(input()))
i = z = 0
for x in q:
	if x%2!=0:
		i+=1
p = zeros(i, dtype=int)
i = 0 
for z in range(0, len(q)):
	if q[z]%2!=0:
		p[i] = z
		i+=1
print(i)
print(p)