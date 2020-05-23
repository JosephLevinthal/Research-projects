from numpy import*
v = array(eval(input("vetor: ")))
m = 0
t = 0
c = 0
while(m>size(v)):
	if(v[m]>0):
		m = m + 1
		v2 = zeros(m)
while(t>size(v)):
	if(v[t]>0):
		v2[c] = v[t]
		t=t+1
		c=c+1
print(v2)
		
		
