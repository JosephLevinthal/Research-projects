from numpy import*
m= array(eval(input("M:")), dtype = int)
v = zeros(7, dtype = int)
for j in range(7):
	v[j] = sum(m[:,j])
for j in range(7):
	if(max(v)== sum(m[:,j])):
		print(j+1)