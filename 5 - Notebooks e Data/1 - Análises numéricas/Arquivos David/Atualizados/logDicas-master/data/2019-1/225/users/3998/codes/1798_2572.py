from numpy import*
x = array(eval(input()))
g= 0

for i in range(size(x)):
	if(x[i]%2 !=0):
		g += 1
v= zeros(g,dtype = int)
h= 0
for i in range(size(x)):
	if(x[i]%2!=0):
		v[h]= x[i]
		h+=1
print(v)