from numpy import * 

p = array(eval((input(""))))

i = 0
j = 0

while i != size(p):
	if p[j] > 80.00:
		p[i] = p[j] + p[j]/(6.67)
	else:
		p[i] = p[j]
		
	i += 1
	j += 1

x = round(sum(p),2)

print(x)
