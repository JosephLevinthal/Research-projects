from numpy import*

ent= array(eval(input("")))
a=0
for i in range(size(ent)):
	if(ent[i]>=2000):
		a+=1
print(a)
m= zeros(a,dtype=int)
j=0
for i in range(size(ent)):
	if(ent[i]>=2000):
		m[j]=i
		j+=1
print(m)