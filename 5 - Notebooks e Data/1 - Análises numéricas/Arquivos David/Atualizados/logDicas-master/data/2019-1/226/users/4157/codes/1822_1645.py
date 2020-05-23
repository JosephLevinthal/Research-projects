from numpy import*
s = array(eval(input("saques:")))
i = 0

for x in range(size(s)):
	if(s[x]>=2000):
		i=i+1
print(i)
v= zeros(i, dtype=int)
b=0
i=0
for z in range(size(s)):
	if(s[z]>=2000):
		v[i]=b
		i=i+1
	b=b+1
print(v)
	
	

	
	