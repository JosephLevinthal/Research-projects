from numpy import*

m = array(eval(input()))
s = 0
for i in range(shape(m)[0]):
	for j in range(shape(m)[1]):
		if(i != j):
			s = s + m[i,j]

print(round(s, 2))